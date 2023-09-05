####### Resizing and Rescaling images & videos ########

import cv2 as cv

frame = cv.VideoCapture('Resources/Videos/dog.mp4')

def rescaleFrame(frame, scale=0.75):

    width = int(frame.shape[1] * scale)
    height = int(frmae.shape[0] * scale)
    
    dimensions = (width, height)

    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

######## reading videos ########

while True:
    isTrue, frame = frame.read()

    frmae_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frmae_resized)
    if cv.waitKey(20) & 0xFF==ord('a'):
        break

frame.release()
cv.destroyAllWindows()

