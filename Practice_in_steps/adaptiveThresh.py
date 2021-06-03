import cv2 as cv

img = cv.imread("photos/ron2.jpg",0)

th1 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,6)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,6)

cv.imshow("img",img)
cv.imshow("thresh",th1)
cv.imshow("Gauss",th2)

cv.waitKey(0)