import cv2
import numpy as np
from matplotlib import pyplot as plt

''' Multiple images are displayed with matplotlib'''

BLUE = [0,0,255]

image = cv2.imread('download.png')

# different type of borders
# parameters(image, widths top,bottom,left,right,border type, value of color if border is constant)

replicate = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(image,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()