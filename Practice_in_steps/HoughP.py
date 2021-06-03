import cv2 as cv
import numpy as np

img = cv.imread("photos/lane1.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
canny = cv.Canny(gray,140,200,apertureSize=3)
cv.imshow("edge",canny)
lines = cv.HoughLinesP(canny,1,np.pi/180,150,minLineLength=100,maxLineGap=3)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()