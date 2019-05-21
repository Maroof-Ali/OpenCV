import numpy as np
import cv2

videoObject = cv2.VideoCapture(0)

while(True):
    ret, frame = videoObject.read()

    # for checking return and frame values 

    print(ret)       # it should reurn true if frame is read correctly.
    print(frame)     # print data contained in a frame

    # Operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #display frame
    cv2.imshow("FRAME", gray)

    # save Frame
    cv2.imwrite("captured_frame.jpg", gray)
    
    if cv2.waitKey(0):
        break

videoObject.release()
cv2.destroyAllWindows()