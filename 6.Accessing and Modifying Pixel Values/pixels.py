import numpy as np
import cv2

image = cv2.imread('messi.jpg')

a_pixel = image[100,100]  # goes to 100th row 100th coloumn, and returns array of BGR
print(a_pixel)            # prints [blue green red] value of that coordinate

# accessing only blue pixel
blue = image[100,100,0]
print(blue)               #returns 116 : RGB image is a 3D array, 0 for 1st slice

# accessing only green pixel
green = image[100,100,1]
print(green)

# accessing only red pixel
red = image[100,100,2]
print(red)


'''
Numpy is a optimized library for fast array calculations.
So simply accessing each and every pixel values and 
modifying it will be very slow and it is discouraged.

'''
''' A better way to modify pixel values'''
print("------------------------------")

#accessing RED value
red_pixel = image.item(50,50,2)
print(red_pixel)

image.itemset((50,50,2),100)
print(image.item(50,50,2))