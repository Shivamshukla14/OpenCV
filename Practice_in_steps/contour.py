import cv2 as cv

img = cv.imread("photos/messi.jpg")
# img = cv.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)),interpolation = cv.INTER_AREA)
open_cv = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
thresh = cv.adaptiveThreshold(open_cv,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,15,7)

contours , hirerchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

print("No. of contours "+ str(len(contours)))

cv.drawContours(img,contours,-1,(0,255,0),1)

cv.imshow("img",img)
cv.imshow("Gray",open_cv) 
cv.imshow("Binary",thresh)
cv.waitKey(0)