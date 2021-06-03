import cv2 as cv

cascade_file = cv.CascadeClassifier("xml/haarcascade_frontalface_default.xml")

cap = cv.VideoCapture(0)

while cap.isOpened():
    _, Frame = cap.read()

    gray = cv.cvtColor(Frame,cv.COLOR_BGR2GRAY)
    faces = cascade_file.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in faces:
        cv.rectangle(Frame,(x,y),(x+w,y+h),(255,0,0),3)

    cv.imshow("image",Frame)
    if cv.waitKey(1) & 0xFF==ord('e'):
        break

cap.release()
cv.destroyAllWindows()