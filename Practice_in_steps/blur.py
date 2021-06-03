import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread("photos/ron2.jpg")
noise = cv.imread("photos/SNPnoise.png")
img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/25

filter2D = cv.filter2D(img,-1,kernel)
blur = cv.blur(img,(5,5))

Gaussian = cv.GaussianBlur(img,(5,5),0)
median = cv.medianBlur(noise,5)

bilateral = cv.bilateralFilter(img,-1,30,200)

images = [img,filter2D,blur,Gaussian,median,noise,bilateral]
titles = ["img","filter2D","blur","Gaussian","median","noise","bilatral"]

for i in range(7):
    plt.subplot(2,4,i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

