import cv2 as cv
import numpy as np

img = cv.imread("photos/messi.jpg")
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

template = cv.imread("photos/messi1.jpg",0)
w, h = template.shape[::-1]

res = cv.matchTemplate(gray_img,template,cv.TM_CCOEFF_NORMED)

threshold = 0.999

loc = np.where(res>=threshold)

for i in zip(*loc[::-1]):
    cv.rectangle(img,i,(i[0]+w,i[1]+h),(0,0,255),1)

cv.imshow("img",img)
cv.waitKey(0)
cv.destroyAllWindows()
