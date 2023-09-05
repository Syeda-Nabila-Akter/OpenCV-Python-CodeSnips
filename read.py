import cv2 as cv

########################################
####### reading images & videos ########
########################################

####### reading images ########
#reading large images is a bit challenging (i.e., cat_large.jpg) due to memory limitations but it can be handled in many ways such as by resizing the image
#img = cv.imread('Resources/Photos/cat.jpg')
#cv.imshow('Cat', img)
#cv.waitKey(0)

######## reading videos ########
# capture = cv.VideoCapture('Resources/Videos/dog.mp4')
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF==ord('a'):
#         break

# capture.release()
# cv.destroyAllWindows()



#######################################################
####### Resizing and Rescaling images & videos ########
#######################################################

def rescaleFrame(frame, scale=0.75)
