import cv2 as cv
import numpy as np
import matplotlib.pylab as plt

def mask_image(img,vertices):
    mask = np.zeros_like(img)
    # chl = img.shape[2]
    count_color = 255
    cv.fillPoly(mask,vertices,count_color)
    masked_image = cv.bitwise_and(img,mask)
    return masked_image

def draw_lines(img,lines):
    img = np.copy(img)
    blank_img = np.zeros((img.shape[0],img.shape[1],3),np.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv.line(img,(x1,y1),(x2,y2),(0,255,0),3)

    img = cv.addWeighted(img,0.8,blank_img,1,0.0)
    return img

# image = cv.imread("photos/lane3.jpg")
# image = cv.cvtColor(image,cv.COLOR_BGR2RGB)
def process(image):
    height = image.shape[0]
    width = image.shape[1]

    pt_vertices = [
        (0,height),
        (650,535),
        (width,height)
    ]

    gray = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
    canny = cv.Canny(gray,100,120)
    result = mask_image(canny,np.array([pt_vertices],np.int32))
    lines = cv.HoughLinesP(result,rho=6,theta=np.pi/60,threshold=140,lines=np.array([]),minLineLength=2,maxLineGap=150)

    result2 = draw_lines(image,lines)
    return result2

cap = cv.VideoCapture("videos/testvideo2.mp4")

while cap.isOpened():
    ret, Frame = cap.read()

    Frame = process(Frame)
    cv.imshow("Frame",Frame)

    if cv.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv.destroyAllWindows()
