import cv2 as cv

img = cv.imread("photos/messi.jpg")

messi = img.copy()

GaussPyr = [messi]
# cv.imshow("Original Image",messi)

for i in range(6):
    messi = cv.pyrDown(messi)
    GaussPyr.append(messi)
    # cv.imshow(str(i),messi)

messi = [GaussPyr[5]]
LapPyr = [messi]

for i in range(5,0,-1):
    Gauss_extended = cv.pyrUp(GaussPyr[i])
    subtracts = cv.subtract(GaussPyr[i-1],Gauss_extended)
    LapPyr.append(subtracts)
    cv.imshow(str(i),subtracts)



cv.waitKey(0)
cv.destroyAllWindows()


