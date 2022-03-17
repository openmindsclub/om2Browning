# This is a sample Python script.
import cv2
import time
import math
import mediapipe as mp
from subprocess import call
cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
mpSOl = mp.solutions.drawing_utils
hands = mphands.Hands(max_num_hands=1)

CTime = 0
PTime = 0

while True:
    sucess,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            #mpSOl.draw_landmarks(img,hand,mphands.HAND_CONNECTIONS)
            for id,lm in enumerate(hand.landmark):
                height ,  width ,  chanel = img.shape
                x , y = int(lm.x*width),int(lm.y*height)
                if id==4:
                    x1 = x
                    y1 = y
                elif id == 8:
                    y2=y
                    x2=x
            cv2.line(img, (x1,y1), (x2,y2),(255,0,255),3)
            length = math.hypot(x2-x1,y2-y1)
            cx,cy = (x1+x2)//2, (y1+y2)//2
            vol = (length * 100) // 175
            if length <= 30:
                vol = 0
                print("Fingers touched : ")
                cv2.circle(img,(cx,cy),15,(0,255,0),cv2.FILLED)
            else:
                print("Not touching")
            if vol>100: vol = 100;
            call(["amixer", "-D", "pulse", "sset", "Master", str(vol)+"%"])
            cv2.putText(img, "volume "+str(int(vol))+"%", (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
    """
    Calculating the FPS
    """
    CTime = time.time()
    fps = 1/(CTime-PTime)
    PTime = CTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
    cv2.imshow("Video record",img)
    if cv2.waitKey(10) & 0XFF == ord("q"):
        break