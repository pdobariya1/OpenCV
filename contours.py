import cv2
import numpy as np

image = cv2.imread('Photos/cats.jpg')
cv2.imshow('Cat', image)

blank = np.zeros(shape=image.shape, dtype=np.uint8)
cv2.imshow('Blank', blank)

gray = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

blur = cv2.GaussianBlur(src=gray, ksize=(5, 5), sigmaX=cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)

canny = cv2.Canny(image=blur, threshold1=125, threshold2=175)
cv2.imshow('Canny Edges', canny)

# ret, thresh = cv2.threshold(src=gray, thresh=125, maxval=255, type=cv2.THRESH_BINARY)
# cv2.imshow('Thresh', thresh)

contours, hierarchies = cv2.findContours(image=canny, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# Draw Contours
cv2.drawContours(image=blank, contours=contours, contourIdx=-1, color=(0, 0, 255), thickness=1)
cv2.imshow('Contours Drawn', blank)

cv2.waitKey(0)