import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

kernel = np.ones((3,3), np.uint8)

img = cv.imread("photos/balls.jpeg",0)

_, th1 = cv.threshold(img,205,255,cv.THRESH_BINARY_INV)

dilation = cv.dilate(th1,kernel,iterations=1)
erosion = cv.erode(dilation,kernel,iterations=2)

opening = cv.morphologyEx(th1,cv.MORPH_OPEN,kernel)
closing = cv.morphologyEx(th1,cv.MORPH_CLOSE,kernel)

mg = cv.morphologyEx(th1,cv.MORPH_GRADIENT,kernel)
th = cv.morphologyEx(th1,cv.MORPH_TOPHAT,kernel)

bh = cv.morphologyEx(th1,cv.MORPH_BLACKHAT,kernel)

images = [img,th1,dilation,erosion,opening,closing,mg,th,bh]
titles = ["img","th1","dilate","erosion","opening","closing","Gradient","th","blackHAt"]

for i in range(9):
    plt.subplot(3,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()