import cv2

image = cv2.imread('Photos/cats.jpg')
cv2.imshow('Image', image)

# Average Blur
average = cv2.blur(src=image, ksize=(3, 3))
cv2.imshow('Average Blur', average)

# Gaussian Blur
gaussian = cv2.GaussianBlur(src=image, ksize=(3, 3), sigmaX=0)
cv2.imshow('Gaussian Blur', gaussian)

# Median Blur
median = cv2.medianBlur(src=image, ksize=3)
cv2.imshow('Median Blur', median)

# Bilateral
bilateral = cv2.bilateralFilter(src=image, d=10, sigmaColor=50, sigmaSpace=25)
cv2.imshow('Bilateral', bilateral)

cv2.waitKey(0)