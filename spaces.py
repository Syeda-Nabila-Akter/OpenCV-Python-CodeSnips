import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources\Photos\park.jpg')
cv.imshow('Park', img)

#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#MATPLOTLIB shows the image as RGB
plt.imshow(img)
plt.show()



#cv.waitKey(0)