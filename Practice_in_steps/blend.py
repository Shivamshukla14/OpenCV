import numpy as np
import cv2 as cv

apple = cv.imread("photos/apple.png")
apple_copy = apple.copy()

gp_apple = [apple_copy]

for i in range(6):
    apple_copy = cv.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

apple_copy = gp_apple[5]
lp_apple = [apple_copy]

for i in range(5,0,-1):
    extended = cv.pyrUp(gp_apple[i])
    lap = cv.subtract(gp_apple[i-1],extended)
    lp_apple.append(lap)
    # cv.imshow(str(i),lap)

orange = cv.imread("photos/orange.jpg")
orange_copy = orange.copy()

gp_orange = [orange_copy]

for i in range(6):
    orange_copy = cv.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

orange_copy = gp_orange[5]
lp_orange = [orange_copy]

for i in range(5,0,-1):
    extended = cv.pyrUp(gp_orange[i])
    lap = cv.subtract(gp_orange[i-1],extended)
    lp_orange.append(lap)

apple_orange_pyramid = []
n = 0

for i,j in zip(lp_apple,lp_orange):
    n += 1
    col, row, chl = i.shape
    lap = np.hstack((i[: ,0:int(col/2)],j[:, int(col/2):]))
    apple_orange_pyramid.append(lap)

apple_orange_reconstruct = apple_orange_pyramid[0]

for i in range(1,6):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_pyramid[i],apple_orange_reconstruct)

cv.imshow("apple_orange_pyr",apple_orange_pyramid[0])
cv.imshow("apple_orange",apple_orange_reconstruct)
cv.waitKey(0)
cv.destroyAllWindows()