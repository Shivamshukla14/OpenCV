import cv2 as cv
import numpy as np

img = cv.imread("photos/Sudoko.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
edges = cv.Canny(gray,50,120,apertureSize=3)
cv.imshow("edges",edges)
lines = cv.HoughLines(edges,1,np.pi/180,200)

for line in lines:
    roh, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * roh
    y0 = a * roh
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()