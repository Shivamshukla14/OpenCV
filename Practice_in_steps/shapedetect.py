import cv2 as cv
import numpy as np

image = cv.imread("photos/smarties.png")
output = image.copy()
gray = cv.cvtColor(output,cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray,5)

circles = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

detected_cirle = np.uint16(np.around(circles))

for (x,y,r) in detected_cirle[0, :]:
    cv.circle(output,(x,y),r,(0,255,0),2)
    cv.circle(output,(x,y),2,(0,0,255),2)

cv.imshow("output",output)
cv.waitKey(0)
cv.destroyAllWindows()