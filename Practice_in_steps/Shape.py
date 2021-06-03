import cv2 as cv

res = cv.imread("photos/shapes.png")
res = cv.resize(res,(int(res.shape[1]/2),int(res.shape[0]/2)),interpolation=cv.INTER_AREA)
img = cv.cvtColor(res,cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(img,240,255,cv.THRESH_BINARY)
contours, _ = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv.approxPolyDP(contour,0.01*cv.arcLength(contour,True),True)
    cv.drawContours(res,[approx],0,(0,0,0),2)
    x = approx.ravel()[0]
    y = approx.ravel()[1]-5
    if len(approx)==3:
        cv.putText(res,"Triangle",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
    elif len(approx)==4:
        (x1,y1,w,h) = cv.boundingRect(approx)
        aspectRatio = float(w)/h
        if aspectRatio >= 0.95 and aspectRatio <=1.05:
            cv.putText(res,"Square",(x1,y1),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
        else:
            cv.putText(res,"Rectangle",(x1,y1),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
    elif len(approx)==5:
        cv.putText(res,"Pentagon",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
    elif len(approx)==6:
        cv.putText(res,"Hexagon",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)
    else:
        cv.putText(res,"Circle",(x,y),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)

cv.imshow("img",res)


cv.waitKey(0)
