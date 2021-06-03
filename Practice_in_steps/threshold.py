import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("photos/grad1.jpg")

_, th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
_, th2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
_, th4 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
_, th5 = cv.threshold(img,127,255,cv.THRESH_TRUNC)

images = [img,th1,th2,th3,th4,th5]
titles = ["normal","binary","binary Inv","ToZero","ToZeroInv","TRUNC"]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
