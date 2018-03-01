import cv2
import os
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread('zebra.jpg',0)
img2=img.copy()
height, width = img.shape[:2]

for i in np.arange(1, height-1):
    for j in np.arange(1, width-1):
        neighbors = []
        for k in np.arange(-1, 2):
            for l in np.arange(-1, 2):
                a = img.item(i+k, j+l)
                neighbors.append(a)
        neighbors.sort()
        median = neighbors[4]
        b = median
        img2.itemset((i,j), b)
cv2.imwrite("zebramedian.jpg",img2)
print "oke"
images = [img,img2]
titles = ['Original Image','Median Image']

for i in xrange(2):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()