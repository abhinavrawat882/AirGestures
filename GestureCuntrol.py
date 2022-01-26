import cv2
import numpy as np
import mediapipe as mp
import time
import win32api
import ctypes
import mouse
vs=cv2.VideoCapture(2)
#getting Vedio Capture from the camera
# here '0' in VideoCapture(0) means to acess frames from camera
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
ret,frame=vs.read()
cTime = 0
pTime = 0
h,w=1168,1760
rn=1
while(True):
    ret,frame=vs.read()
    #reading frames 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame=cv2.flip(frame, 1)
    #need to flip the frame to get natural vedio to paint
    results = hands.process(frame)
    
    #print(results)
    
    #break
    #shows the vedio frame by frame
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            #print(list(enumerate(handlms.landmark)))
            a=list(enumerate(handlms.landmark))
            #index fingure== 8
            x=a[8][1].x*w
            y=a[8][1].y*h
            win32api.SetCursorPos((int(x),int(y)))
            #thumb
            cxt=a[4][1].x*w
            cyt=a[4][1].y*h
            #print("1     ",((cxt-x)**2+(cyt-y)**2)**0.5 )
            if ((cxt-x)**2+(cyt-y)**2)**0.5 <=45 :
                mouse.click('left')
            cx1=a[12][1].x*w
            cy1=a[12][1].y*h
            cx2=a[16][1].x*w
            cy2=a[16][1].y*h
            x0=a[0][1].x*w
            y0=a[0][1].y*h
            #print(((cx1-x0)**2+(cy1-y0)**2)**0.5 )
            #print(((cx2-x0)**2+(cy2-y0)**2)**0.5)
            #if ((cx1-x0)**2+(cy1-y0)**2)**0.5 <=120  and ((cx2-x0)**2+(cy2-y0)**2)**0.5 <=120 :
            #    rn=1
            mpDraw.draw_landmarks(frame, handlms)
    if(rn==2):
        break
    #cv2.putText(frame, str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX, 3, (120,0,0), 3)
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
vs.release()
#cv2.destroyAllWindows()
