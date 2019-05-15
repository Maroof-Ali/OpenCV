import numpy as np
import cv2

videoObject = cv2.VideoCapture('drop.avi')

while(videoObject.isOpened()):

    ret, frame = videoObject.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Video File", gray)

    if cv2.waitKey(20) & 0xFF == ord('q'): # q for quit, 0xFF for bit transformation, 20 to 25 milliseconds is OK
        break

videoObject.release()
cv2.destroyAllWindows()