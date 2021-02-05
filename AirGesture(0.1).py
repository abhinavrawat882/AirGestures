import cv2
import numpy as np
import imutils


vs=cv2.VideoCapture(0)
#getting Vedio Capture from the camera
# here '0' in VideoCapture(0) means to acess frames from camera

ret,frame=vs.read()

paintWindow = frame*0 +255
#paint windows where you will see paint 
#its completely white 
#first we made thw frame dark thn added 255 to make it white 


upper_blue = np.array([153, 255, 255])
lower_blue = np.array([74, 82, 59])
#tells hsv range of blue colour so that it can be extracted and tracked

while(True):
    ret,frame=vs.read()
    #reading frames 

    frame=cv2.flip(frame, 1)
    #need to flip the frame to get natural vedio to paint
    
    cv2.imshow('frame',frame)
    #shows the vedio frame by frame
    
    cv2.imshow('frame',paintWindow)
    
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
vs.release()
cv2.destroyAllWindows()
