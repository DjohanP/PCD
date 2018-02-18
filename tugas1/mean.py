import cv2
import os
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread('856876.fig.001b.jpg',0)
img2=img.copy()
height, width = img.shape[:2]

for i in np.arange(3, height-3):
    for j in np.arange(3, width-3):
        neighbors = []
        for k in np.arange(-3, 4):
            for l in np.arange(-3, 4):
                a = img.item(i+k, j+l)
                neighbors.append(a)
        neighbors.sort()
        median = neighbors[24]
        b = median
        img2.itemset((i,j), b)
print "oke"
images = [img,img2]
titles = ['Original Image','Median Image']

for i in xrange(2):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()