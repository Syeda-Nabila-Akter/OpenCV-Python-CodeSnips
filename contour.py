import cv2 as cv
import numpy as np
  
image = cv.imread('Resources/Photos/cat.jpg')
cv.waitKey(0)
  
# Grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
  
# Find Canny edges
canny = cv.Canny(gray, 30, 200)
cv.waitKey(0)
  
# Finding Contours
# Use a copy of the image e.g. edged.copy()
# since findContours alters the image
contours, hierarchy = cv.findContours(canny, 
    cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
  
cv.imshow('Canny Edges After Contouring', canny)
#cv.waitKey(0)
  
print("Number of Contours found = " + str(len(contours)))
  
# Draw all contours
# -1 signifies drawing all contours
cv.drawContours(image, contours, -1, (0, 0, 255), 1)
  
cv.imshow('Contours', image)
cv.waitKey(0)
cv.destroyAllWindows()