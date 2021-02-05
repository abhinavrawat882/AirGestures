import cv2
import numpy as np
import imutils


vs=cv2.VideoCapture(0)
#getting Vedio Capture from the camera
# here '0' in VideoCapture(0) means to acess frames from camera

while(True):
    ret,frame=vs.read()
    #reading frames 

    frame=cv2.flip(frame, 1)
    
    cv2.imshow('frame',frame)
    #shows the vedio frame by frame

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
vs.release()
cv2.destroyAllWindows()
