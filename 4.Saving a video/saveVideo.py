import numpy as np
import cv2

videoObject = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640, 480)) #(filename, codec, fps, resolution)

while(videoObject.isOpened()):
    ret, frame = videoObject.read()
    
    if ret == True:
        #frame = cv2.flip(frame,0)   # for flipping frame

        print(frame)        #prints captured video stream on console
        out.write(frame)

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break



videoObject.release()
out.release()
cv2.destroyAllWindows()