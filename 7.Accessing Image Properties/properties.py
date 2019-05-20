import numpy as np
import cv2

'''
image.dtype is very important while debugging because 
a large number of errors in OpenCV-Python code is caused by invalid datatype.
'''
# For color image

color_image = cv2.imread('joker.jpg')
print(color_image.shape)
print(color_image.size)                  # display total number of pixels
print(color_image.dtype)

print("---------------------------------")

# convert color to grayscale image

gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
print(gray_image.shape)
print(gray_image.size)
print(gray_image.dtype)

cv2.imshow('Joker', color_image)
cv2.waitKey(0)
cv2.imshow('Joker', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()