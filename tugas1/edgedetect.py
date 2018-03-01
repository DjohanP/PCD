import cv2
from matplotlib import pyplot as plt

img = cv2.imread('degea.jpg', 0)
edges = cv2.Canny(img, 255, 255)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
cv2.imwrite("degeadetect.jpg",edges)
plt.show()
