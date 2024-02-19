import cv2
import numpy as np

image = cv2.imread('Photos/park.jpg')
cv2.imshow('Image', image)

blank = np.zeros(image.shape[:2], dtype=np.uint8)

# Split into 3 channel
b, g, r = cv2.split(image)
cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)

# Merge 3 channel
merge = cv2.merge([b, g, r])
cv2.imshow('Merge Image', merge)

blue = cv2.merge([b, blank, blank])
green = cv2.merge([blank, g, blank])
red = cv2.merge([blank, blank, r])

cv2.imshow('Blue', blue)
cv2.imshow('Green', green)
cv2.imshow('Red', red)

# Shape
print(f"Original Image : {image.shape}")
print(f"Blue Image : {b.shape}")
print(f"Green Image : {g.shape}")
print(f"Red Image : {r.shape}")

cv2.waitKey(0)