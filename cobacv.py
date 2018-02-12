import cv2
import os
import numpy as np

def invert(image,name):
	image=abs(255-image)
	cv2.imwrite(name,image)

def invert2(image,name):
	for x in np.nditer(image,op_flags=['readwrite']):
		x=abs(x-255)
	cv2.imwrite(name,image)

original=str("gambar1.png")
image=cv2.imread(original)
gray_im=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
invert(gray_im,"negative.jpg")
invert2(gray_im,"negative2.jpg")
