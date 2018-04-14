from PyQt5 import QtCore, QtGui, QtWidgets
import queue
import os
import imghdr
from Efx import Efx
from threading import Thread

class Ui_MainWindow(object):
    
    def __init__(self):
        self.imgExts = ['bmp','dib','jpg','jpeg','jpe','jp2','png','pbm','pgm','ppm','sr','ras','tff','tif']    
        self.pathQueue = []
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pbOpenDestFolder = QtWidgets.QPushButton(self.centralwidget)
        self.pbOpenDestFolder.setObjectName("pbOpenDestFolder")
        self.gridLayout.addWidget(self.pbOpenDestFolder, 1, 2, 1, 1)
        self.leDestPath = QtWidgets.QLineEdit(self.centralwidget)
        self.leDestPath.setReadOnly(True)
        self.leDestPath.setObjectName("leDestPath")
        self.gridLayout.addWidget(self.leDestPath, 1, 1, 1, 1)
        self.pbOpenSrcFolder = QtWidgets.QPushButton(self.centralwidget)
        self.pbOpenSrcFolder.setObjectName("pbOpenSrcFolder")
        self.gridLayout.addWidget(self.pbOpenSrcFolder, 0, 2, 1, 1)
        self.leSrcPath = QtWidgets.QLineEdit(self.centralwidget)
        self.leSrcPath.setReadOnly(True)
        self.leSrcPath.setObjectName("leSrcPath")
        self.gridLayout.addWidget(self.leSrcPath, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cbFlipH = QtWidgets.QCheckBox(self.centralwidget)
        self.cbFlipH.setObjectName("cbFlipH")
        self.gridLayout_2.addWidget(self.cbFlipH, 0, 1, 1, 1)
        self.cbBlur = QtWidgets.QCheckBox(self.centralwidget)
        self.cbBlur.setObjectName("cbBlur")
        self.gridLayout_2.addWidget(self.cbBlur, 2, 1, 1, 1)
        self.cbFlipV = QtWidgets.QCheckBox(self.centralwidget)
        self.cbFlipV.setObjectName("cbFlipV")
        self.gridLayout_2.addWidget(self.cbFlipV, 1, 1, 1, 1)
        self.cbGrayScale = QtWidgets.QCheckBox(self.centralwidget)
        self.cbGrayScale.setObjectName("cbGrayScale")
        self.gridLayout_2.addWidget(self.cbGrayScale, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.pbApply = QtWidgets.QPushButton(self.centralwidget)
        self.pbApply.setObjectName("pbApply")
        self.verticalLayout.addWidget(self.pbApply)
        self.lbQtdImages = QtWidgets.QLabel(self.centralwidget)
        self.lbQtdImages.setObjectName("lbQtdImages")
        self.verticalLayout.addWidget(self.lbQtdImages)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.pbStatus = QtWidgets.QProgressBar(self.centralwidget)
        self.pbStatus.setProperty("value", 24)
        self.pbStatus.setObjectName("pbStatus")
        self.verticalLayout.addWidget(self.pbStatus)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 21))
        self.menubar.setObjectName("menubar")
        self.menuFIles = QtWidgets.QMenu(self.menubar)
        self.menuFIles.setObjectName("menuFIles")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionInput_Path = QtWidgets.QAction(MainWindow)
        self.actionInput_Path.setObjectName("actionInput_Path")
        self.actionOutput_Path = QtWidgets.QAction(MainWindow)
        self.actionOutput_Path.setObjectName("actionOutput_Path")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFIles.addAction(self.actionExit)
        self.menubar.addAction(self.menuFIles.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.setSignals()
        self.init_frm()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pbOpenDestFolder.setText(_translate("MainWindow", "Open"))
        self.pbOpenSrcFolder.setText(_translate("MainWindow", "Open"))
        self.label_2.setText(_translate("MainWindow", "Dest Folder"))
        self.label.setText(_translate("MainWindow", "Src Folder"))
        self.cbFlipH.setText(_translate("MainWindow", "Flip Horizontal"))
        self.cbBlur.setText(_translate("MainWindow", "Blur"))
        self.cbFlipV.setText(_translate("MainWindow", "Flip Verical"))
        self.cbGrayScale.setText(_translate("MainWindow", "Grayscale"))
        self.pbApply.setText(_translate("MainWindow", "Apply"))
        self.lbQtdImages.setText(_translate("MainWindow", "0 Images"))
        self.menuFIles.setTitle(_translate("MainWindow", "Files"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionInput_Path.setText(_translate("MainWindow", "Input Path"))
        self.actionOutput_Path.setText(_translate("MainWindow", "Output Path"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def setSignals(self):
        self.pbApply.clicked.connect(self.onClicked_Apply)
        self.pbOpenSrcFolder.clicked.connect(self.onClicked_SrcPath)
        self.pbOpenDestFolder.clicked.connect(self.onClicked_DestPath)

    def openFolder(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode())
        dir = dialog.getExistingDirectory(None,'Open a folder')
        return dir

    def init_frm(self):
        self.pbApply.setEnabled(False)
        self.pbStatus.setValue(100)

    
    def setEnableCtrs(self,enable):
        self.pbApply.setEnabled(enable)
        self.pbOpenSrcFolder.setEnabled(enable)
        self.pbOpenDestFolder.setEnabled(enable)

    def enableBtnApply(self):
        srcPath = self.leSrcPath.text()
        destPath = self.leDestPath.text()
        if len(srcPath) > 0 and len(destPath) > 0:
            self.pbApply.setEnabled(True)        
        else:
            self.pbApply.setEnabled(False) 

    def onClicked_SrcPath(self):
        self.leSrcPath.setText(self.openFolder())
        self.enableBtnApply()

    def onClicked_DestPath(self):
        path = self.openFolder()
        self.leDestPath.setText(path)
        self.enableBtnApply()
        paths = ""
        for root,dirs,files in os.walk(path):
            for filename in files:
                x = os.path.join(root,filename)
                if os.path.isfile(x):
                    for ext in self.imgExts:
                        if imghdr.what(x) == ext:
                            paths += x + '\n'
                            queue.heappush(self.pathQueue,x)
                            break
        self.plainTextEdit.setPlainText(paths)

    def onClicked_Apply(self):
        while len(self.pathQueue) > 0:
            path = queue.heappop(self.pathQueue)
            if self.cbFlipH.isChecked:
                self.generate_thread(path,0)
            if self.cbFlipV.isChecked:
                self.generate_thread(path,1)
            if self.cbBlur.isChecked:
                self.generate_thread(path,2)
            if self.cbGrayScale.isChecked:
                self.generate_thread(path,3)


    def generate_thread(self,src,efx):
        dest = self.leDestPath.text()
        efx = Efx(src,dest)
        th = Thread



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())