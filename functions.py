import cv2 as cv

img = cv.imread('Resources\Photos\cat.jpg')

cv.imshow('Cat', img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blurring image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

#edge in blur image
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges in Blur Image', canny) #blur image has reduced edge line

#Dialating image
dilated = cv.dilate(canny, (3,3), iterations=5)
cv.imshow("Dilated image", dilated)

#Eroding image
eroded = cv.erode(dialated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

#Resize 
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA) #Inter_cubic -> for rescaling
cv.imshow('Resized', resized)

#Croping
cropped = img[50:200, 200:300]
cv.imshow('Cropped', cropped)


cv.waitKey(0)