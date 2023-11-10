import cv2
import numpy as np

# Create Blank Image
blank = np.zeros((500, 500, 3), dtype=np.uint8)  # (height, width, color_channel), uint = DataType of Image
# cv2.imshow('Blank', blank)

# 1. Paint the image a certain color
# blank[150:300, 300:355] = 0, 0, 255  # (255,0,0=Blue) (0,255,0=Green) (0,0,255=Red)
# cv2.imshow('Red', blank)

# 2. Draw a Rectangle
cv2.rectangle(img=blank, pt1=(0, 0), pt2=(250, 150), color=(0, 0, 255), thickness=cv2.FILLED)
cv2.imshow('Rectangle', blank)

# 3. Draw a Circle
cv2.circle(img=blank, center=(blank.shape[1]//2, blank.shape[0]//2), radius=40, color=(0, 255, 0), thickness=cv2.FILLED)
cv2.imshow('Circle', blank)

# 4. Draw a Line
cv2.line(img=blank, pt1=(250, 250), pt2=(500, 500), color=(255, 0, 0), thickness=5)
cv2.imshow('Line', blank)

# 5. Write Text
cv2.putText(
    img=blank, text='Hello..!!', org=(200, 250), fontFace=cv2.FONT_HERSHEY_TRIPLEX, 
    fontScale=1.0, color=(0, 0, 255), thickness=2
)
cv2.imshow('Text', blank)

cv2.waitKey(0)
