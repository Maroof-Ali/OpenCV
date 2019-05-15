import numpy as np
import cv2

myImage = cv2.imread("messi.jpg",0) #1,0,-1

#image covers whole screen
#cv2.namedWindow("Messi", cv2.WINDOW_NORMAL)
#image display in orignal resolution, by default this flag is set
#cv2.namedWindow("Messi", cv2.WINDOW_AUTOSIZE)

cv2.imshow('Messi',myImage)   #image display in grey scale mode
cv2.waitKey(0)
cv2.destroyAllWindows()

# write an image

cv2.imwrite('messiGray.png', myImage)

