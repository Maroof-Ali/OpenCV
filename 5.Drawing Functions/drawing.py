import numpy as np
import cv2

img = np.zeros((600,600,3), np.uint8) #create a blank black image

# create a line on Image
img = cv2.line(img, (0,0), (599,599), (224,194,47), 3) #(image, start-point,endpoint,color in BGR,line thickness)

#create a rectangle on image
#(image, top-left corner, bottom-right corner, color in BGR, thickness)
img = cv2.rectangle(img,(384,0),(550,128),(0,255,0),3)

# create a circle
#(image, center cordinates, radius, color, thickness )
img = cv2.circle(img,(447,200), 63, (0,0,255), -1)      # -1 for filling the circle

#adding text to images
#(image,text,bottom-left corner,font-family,font-size,color,line-type)
font = cv2.putText(img,"Maroof Ali : OpenCV", (10,500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),2,cv2.LINE_AA)


cv2.imshow("IMAGE with Line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
