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

cv.waitKey(0)