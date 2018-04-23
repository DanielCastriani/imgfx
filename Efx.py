import cv2
import numpy as np

class Efx:
    def __init__(self,imgSrc,name):
        self.imgSrc = imgSrc
        self.name = name
    
    def filpH(self,destPath,name):
        destImg = cv2.flip(self.imgSrc,0)
        cv2.imwrite(destPath+"/"+ name+ "_FlipH.png",destImg)        

    def filpV(self,destPath,name):   
        destImg = cv2.flip(self.imgSrc,1)             
        cv2.imwrite(destPath+"/"+ name+"_FlipV.png",destImg)

    def grayScale(self,destPath,name):
        destImg = cv2.cvtColor(self.imgSrc,cv2.COLOR_BGR2GRAY)        
        cv2.imwrite(destPath+"/"+ name+ "_Grayscale.png",destImg)
    
    def blur(self,destPath,name):
        destImg = cv2.blur(self.imgSrc,(5,5))      
        cv2.imwrite(destPath+"/"+ name+ "_blur.png",destImg)

    def filter_brightnes_contrast(self,destPath,name,brightness,contrast):
        """g(x) = contrast*f(x) + brightness"""
        hsv = cv2.addWeighted(self.imgSrc,contrast,np.zeros(self.imgSrc.shape,self.imgSrc.dtype),0,brightness)
        t = " [Brightness,Contrast] [" + str(brightness)+ "," + str(contrast) + "]"
        cv2.imwrite(destPath+"/" + name + " " + t + "_.png",hsv)