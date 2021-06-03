from typing import no_type_check
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread("photos/ron2.jpg",0)

Lap = cv.Laplacian(img,cv.CV_64F,ksize=3)
Lap = np.uint8(np.absolute(Lap))

soblex = cv.Sobel(img,cv.CV_64F,1,0)
sobley = cv.Sobel(img,cv.CV_64F,0,1)

soblex = np.uint8(np.absolute(soblex))
sobley = np.uint8(np.absolute(sobley))

soblexy = cv.bitwise_or(soblex,sobley)

canny = cv.Canny(img,70,150)

images = [img,Lap,soblex,sobley,soblexy,canny]
titles  = ["img","Laplacian","soblex","sobley","soblexy","canny"]



for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()