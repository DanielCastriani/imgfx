# pylint: disable=E1101
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
from Efx import Efx
from UI.mainWindow import Ui_MainWindow
import queue
import os
import imghdr
import cv2
import re
import sys,time
import numpy as np

class MainWindowController(object):
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.pathQueue = []
        self.__setup()
        self.init_frm()

    def __setup(self):
        self.ui.pbApply.clicked.connect(self.onClicked_Apply)
        self.ui.pbOpenSrcFolder.clicked.connect(self.onClicked_SrcPath)
        self.ui.pbOpenDestFolder.clicked.connect(self.onClicked_DestPath)

    def openFolder(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode())
        dir = dialog.getExistingDirectory(None,'Open a folder')
        return dir

    def init_frm(self):
        self.ui.pbApply.setEnabled(False)
        self.ui.pbStatus.setValue(100)

    def setEnableCtrs(self,enable):
        self.ui.pbApply.setEnabled(enable)
        self.ui.pbOpenSrcFolder.setEnabled(enable)
        self.ui.pbOpenDestFolder.setEnabled(enable)

    def enableBtnApply(self):
        srcPath = self.ui.leSrcPath.text()
        destPath = self.ui.leDestPath.text()
        if len(srcPath) > 0 and len(destPath) > 0:
            self.ui.pbApply.setEnabled(True)
        else:
            self.ui.pbApply.setEnabled(False)

    def onClicked_SrcPath(self):
        path = self.openFolder()
        self.ui.leSrcPath.setText(path)
        self.enableBtnApply()
        paths = ""
        for root,_,files in os.walk(path):
            for filename in files:
                x = os.path.join(root,filename)
                if os.path.isfile(x) :
                    isImg = imghdr.what(x)
                    if isImg:
                        paths += x + '\n'
                        queue.heappush(self.pathQueue,x)
                    else:
                        print('Not an image')
        self.ui.plainTextEdit.setPlainText(paths)

    def onClicked_DestPath(self):
        self.ui.leDestPath.setText(self.openFolder())
        self.enableBtnApply()

    def onClicked_Apply(self):
        self.ui.pbStatus.setMaximum(len(self.pathQueue))
        qtd = 0
        dest = self.ui.leDestPath.text().replace("\\","/")
        while len(self.pathQueue) > 0:
            path = queue.heappop(self.pathQueue)
            path = path.replace("\\","/")
            srcImg = cv2.imread(path)
            if(srcImg is None):
                print("Imagem nula:",path)
            else:
                #name = re.split("\\\\|\/|\.",path)[-2]               

                aux_name = re.split('\/',path)[-1]
                name = ''
                for i in range(len(aux_name) - 4):
                    name += aux_name[i]

                efx = Efx(srcImg,name)

                if self.ui.cbFlipH.isChecked():
                    efx.filpH(dest,name)
                if self.ui.cbFlipV.isChecked():
                    efx.filpV(dest,name)
                if self.ui.cbBlur.isChecked():
                    efx.blur(dest,name)
                if self.ui.cbGrayScale.isChecked():
                    efx.grayScale(dest,name)

                if self.ui.cbBrightness.isChecked():
                    efx.filter_brightnes_contrast(dest,name,30,1)
                    efx.filter_brightnes_contrast(dest,name,-30,1)
                    efx.filter_brightnes_contrast(dest,name,50,1)
                    efx.filter_brightnes_contrast(dest,name,-50,1)
                    efx.filter_brightnes_contrast(dest,name,80,1)
                    efx.filter_brightnes_contrast(dest,name,-80,1)

                if self.ui.cbContrast.isChecked():
                    efx.filter_brightnes_contrast(dest,name,0,0.6)
                    efx.filter_brightnes_contrast(dest,name,0,0.7)
                    efx.filter_brightnes_contrast(dest,name,0,0.8)
                    efx.filter_brightnes_contrast(dest,name,0,1.2)
                    efx.filter_brightnes_contrast(dest,name,0,1.3)
                    efx.filter_brightnes_contrast(dest,name,0,1.4)

                if self.ui.cbRotationAnt.isChecked():
                    efx.rotate(dest,name,-10)
                    efx.rotate(dest,name,-15)

                if self.ui.cbRotationAnt.isChecked():
                    efx.rotate(dest,name,10)
                    efx.rotate(dest,name,15)

            qtd+=1
            self.ui.pbStatus.setValue(qtd)
        self.ui.plainTextEdit.setPlainText("Finished")

if __name__ == "__main__":
    ctr = MainWindowController()
    ctr.MainWindow.show()
    sys.exit(ctr.app.exec_())
