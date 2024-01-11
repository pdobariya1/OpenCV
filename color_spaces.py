import cv2
import matplotlib.pyplot as plt

# OpenCV show BGR format by default
image = cv2.imread('Photos/park.jpg')
cv2.imshow('Park', image)

# Matplotlib show RGB format by default
# plt.imshow(image)
# plt.show()

# BGR to Gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)

# BGR to l*a*b
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB', lab)

# BGR to RGB
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()

cv2.waitKey(0)