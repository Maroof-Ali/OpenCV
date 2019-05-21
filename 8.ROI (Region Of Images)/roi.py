import numpy as np
import cv2

''' Pick a region and copy it to a particular area in image'''

image = cv2.imread('messi.jpg')
print(image.shape)
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

region = image[30:80,100:150]   # picks a particular region from image

image[100:150,10:60] = region   # puts the picked region in image
cv2.imshow('Modeified Frame', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

''' Spliting image into channels'''
blue,green,red = cv2.split(image)
#OR
blue = image[:,:,0]
green = image[:,:,1]
red = image[:,:,2]      # Remember cv2.split() is costly operation, numpy indexing is effecient

''' Changing All Blue Pixels to zero '''

image[:,:,0] = 0        # means all rows,all coloumns,1st slice

cv2.imshow('Zero Blue Frame', image)
cv2.waitKey(0)
cv2.destroyAllWindows()