import cv2
import numpy as np

blank = np.zeros(shape=(400, 400), dtype=np.uint8)

rectangle = cv2.rectangle(img=blank.copy(), pt1=(30, 30), pt2=(370, 370), color=255, thickness=-1)
circle = cv2.circle(img=blank.copy(), center=(200, 200), radius=200, color=255, thickness=-1)

cv2.imshow('Rectangle', rectangle)
cv2.imshow('Circle', circle)

# Bitwise AND -> intersecting region
bitwise_and = cv2.bitwise_and(src1=rectangle, src2=circle)
cv2.imshow('Bitwise AND', bitwise_and)

# Bitwise OR -> non-intersecting & intersecting region
bitwise_or = cv2.bitwise_or(src1=rectangle, src2=circle)
cv2.imshow('Bitwise OR', bitwise_or)

# Bitwise XOR -> non-intersecting region
bitwise_xor = cv2.bitwise_xor(src1=rectangle, src2=circle)
cv2.imshow('Bitwise XOR', bitwise_xor)

# Bitwise NOT
bitwise_not = cv2.bitwise_not(src=rectangle)
cv2.imshow('Bitwise NOT', bitwise_not)

cv2.waitKey(0)