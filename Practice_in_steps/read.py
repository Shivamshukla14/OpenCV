import cv2 as cv
from matplotlib import pyplot as plt




# img = cv.imread("photos/ron2.jpg",cv.IMREAD_GRAYSCALE)


# cv.imshow("img",img)

# img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.show()

# cv.waitKey(0)

cap = cv.VideoCapture("videos/a.mp4")

while True:
    isTrue, Frame = cap.read()

    cv.imshow("Frame",Frame)

    if cv.waitKey(20) & 0xFF==ord('e'):
        break

cap.release()
cv.destroyAllWindows()
