# pylint: disable=E1101
import cv2
import numpy as np

class Efx:
    def __init__(self,imgSrc,name):
        self.imgSrc = imgSrc
        self.name = name

    def filpH(self,destPath,name):
        destImg = cv2.flip(self.imgSrc,0)
        self.save(destImg,destPath,name,"FlipH")

    def filpV(self,destPath,name):
        destImg = cv2.flip(self.imgSrc,1)
        self.save(destImg,destPath,name,"FlipV")

    def grayScale(self,destPath,name):
        destImg = cv2.cvtColor(self.imgSrc,cv2.COLOR_BGR2GRAY)
        self.save(destImg,destPath,name,"Grayscale")

    def blur(self,destPath,name):
        destImg = cv2.blur(self.imgSrc,(5,5))
        self.save(destImg,destPath,name,"blur")

    def filter_brightnes_contrast(self,destPath,name,brightness,contrast):
        """g(x) = contrast*f(x) + brightness"""
        hsv = cv2.addWeighted(self.imgSrc,contrast,np.zeros(self.imgSrc.shape,self.imgSrc.dtype),0,brightness)
        t = "[Brightness,Contrast] [" + str(brightness)+ "," + str(contrast) + "]"
        # cv2.imwrite(destPath+"/" + name + t + ".png",hsv)
        self.save(hsv,destPath,name,t)

    def rotate(self,destPath,name,angle):
        rows,cols,ch = self.imgSrc.shape
        M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
        destImg = cv2.warpAffine(self.imgSrc,M,(cols,rows))
        self.save(destImg,destPath,name,"rotate[" + str(angle) +"]")

    def save(self,img,dest,name,opr):
        cv2.imwrite(dest+"/"+ name + " _" + opr + ".png",img) 
