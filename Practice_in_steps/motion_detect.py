import cv2 as cv

cap = cv.VideoCapture("videos/vtest.avi")

ret, Frame1 = cap.read()
ret, Frame2 = cap.read()

while cap.isOpened():
    diff = cv.absdiff(Frame1,Frame2)
    gray = cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    _,thresh = cv.threshold(gray,30,255,0)
    dilate = cv.dilate(thresh,None,iterations=3)
    contour, _ = cv.findContours(dilate,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    for con in contour:
        (x,y,w,h) = cv.boundingRect(con)
        if cv.contourArea(con)<800:
            continue
        cv.rectangle(Frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv.putText(Frame1,"Status: {}".format('Movement'),(10,20),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv.imshow("Motion",Frame1)

    Frame1 = Frame2
    ret, Frame2 = cap.read()



    if cv.waitKey(40) & 0xFF==ord('e'):
        break

cap.release()
cv.destroyAllWindows()