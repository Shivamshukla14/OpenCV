import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("photos/messi.jpg",0)

hist = cv.calcHist([img], [0], None, [256], [0,256])

plt.plot(hist)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()