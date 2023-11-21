import cv2
import numpy as np

image = cv2.imread('Photos/park.jpg')
cv2.imshow('Park', image)

# Translation
def translate(image, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (image.shape[1], image.shape[0])
    return cv2.warpAffine(image, transMat, dimensions)

"""
x  --> Right
y  --> Down
-x --> Left
-y --> Up
"""
translated = translate(image, 100, 100)
cv2.imshow('Translated', translated)


# Rotation
def rotate(image, angle, rotPoint=None):
    (height, width) = image.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    
    return cv2.warpAffine(image, rotMat, dimensions)

rotated = rotate(image, -90)
cv2.imshow('Rotated', rotated)

# rotated_rotated = rotate(rotated, 45)
# cv2.imshow('Rotated Rotated', rotated_rotated)


# Flipping
"""
1 = flippping image horizontally
0 = flippping image vertically
-1 = flippping image both side
"""
flip = cv2.flip(src=image, flipCode=1)
cv2.imshow('Flip', flip)


# Cropping
cropped = image[100:300, 300:500]
cv2.imshow('Cropped', cropped)


cv2.waitKey(0)
