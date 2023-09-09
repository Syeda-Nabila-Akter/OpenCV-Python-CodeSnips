import cv2 as cv
import numpy as np

img = cv.imread('Resources\Photos\park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
red = cv.merge([blank, blank, r])
green = cv.merge([blank, g, blank])

cv.imshow('Blue', blue)
cv.imshow('Red', red)
cv.imshow('Green', green)

# cv.imshow('Blue', b)
# cv.imshow('green', g)
# cv.imshow('Red', r)

# print(img.shape) #it has 3 color aspects, so output is 3
# print(b.shape) #it has 1 color aspect, output 1
# print(g.shape) #it has 1 color aspect, output 1
# print(r.shape) #it has 1 color aspect, output 1

merged = cv.merge([b, g, r])
# cv.imshow('Merged', merged)

cv.waitKey(0)