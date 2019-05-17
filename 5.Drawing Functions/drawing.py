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
img = cv2.putText(img,"Maroof Ali : OpenCV", (10,500), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),2,cv2.LINE_AA)

#adding ellipse
#(image,center of ellipse,length of major and minor axis,angle,color,thickness)
img = cv2.ellipse(img,(490,350),(100,50),0,0,360,(255,255,255),3)

#adding a polygon
    #create array of points, shape (rows,1,2)
    #(image,array of points, True or False,color)
points =  np.array([[15,10],[20,30],[70,20],[50,10]], np.int32)
points = points.reshape((-1,1,2))
img = cv2.polylines(img,[points],True,(0,255,200)) #True for close shape, False for open polygon


cv2.imshow("IMAGE with Line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
