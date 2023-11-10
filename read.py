import cv2

def rescaleFrame(frame, scale=0.75):
    # Photos, Videos & Live Videos
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (height, width)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

def changeRes(height, width):
    # Live Videos
    capture.set(4, height)
    capture.set(3, width)

# Reading photo
image = cv2.imread('Photos/cat.jpg')
image_resized = rescaleFrame(image)
cv2.imshow('Cat', image)
cv2.imshow('Image_Resized', image_resized)
cv2.waitKey(0)

# Reading video
capture = cv2.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.20)
    cv2.imshow('Video', frame)
    cv2.imshow('Resized_video', frame_resized)
    if cv2.waitKey(20) & 0xff==ord('d'):
        break
capture.release()
cv2.destroyAllWindows()


