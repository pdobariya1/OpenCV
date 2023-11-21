import cv2
import numpy as np

# Read image
image = cv2.imread("Photos\park.jpg")
cv2.imshow('Image', image)

print(f"Shape of Image : {image.shape}")

# Converting into gray-scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# Blur image
gauss_blur = cv2.GaussianBlur(src=image, ksize=(5, 5), sigmaX=cv2.BORDER_DEFAULT)
cv2.imshow('Gaussian Blur', gauss_blur)

# Edge cascade
canny = cv2.Canny(image=gauss_blur, threshold1=120, threshold2=150)
cv2.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv2.dilate(src=canny, kernel=(5, 5), iterations=2)
cv2.imshow('Dilated', dilated)

# Eroding
eroded = cv2.erode(src=dilated, kernel=(3, 3), iterations=2)
cv2.imshow('Eroded', eroded)

# Resize
resized = cv2.resize(src=image, dsize=(500, 400), interpolation=cv2.INTER_LINEAR)
cv2.imshow('Resized', resized)

# Cropping
cropped = image[100:300, 200:500]
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)
