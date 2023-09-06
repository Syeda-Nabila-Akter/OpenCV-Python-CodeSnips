import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') #(500,500,3) -> (height, width, color channel)
cv.imshow('Blank', blank)

#paint the image in different color
blank[:] = 0,255,0
cv.imshow('Green', blank)

#draw image within image
blank[200:300, 300:400] = 0,0,255
cv.imshow('Red in Black', blank)

#draw rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness = 2)
cv.imshow('Rectangle', blank)

#draw circle
cv.circle(blank, (255, 255), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

#draw line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=1)
cv.imshow('Line', blank)

#Write text on image
cv.putText(blank, 'Hello world', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)


cv.waitKey(0)