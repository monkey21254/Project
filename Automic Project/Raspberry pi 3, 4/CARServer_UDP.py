# CARServer_UDP.py
import CARControl_UDP
from socket import *
from time import ctime
import RPi.GPIO as GPIO
import sys
import cv2
import time
# Set the color recognition range
# If you want a different color, change it.(Blue)
Color_Lower = (70,100,70)
Color_Upper = (92, 255, 255)

# Camera Frame Range and Setting
Frame_Width  = 320
Frame_Height = 240
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH,  Frame_Width)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, Frame_Height)

# destination=0

def draw(contours, center_list, frame):
    if len(contours) > 0:
        # Find the max length of contours
        c = max(contours, key=cv2.contourArea)
        # Find the x, y, radius of given contours       
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        
        # Find the moments
        M = cv2.moments(c)
        try:
           # mass center
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            center_list[i] = center
           # process every frame
            cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            
            rows, cols = mask.shape[:2]
            [vx, vy, x,y] = cv2.fitLine(c, cv2.DIST_L2, 0, 0.01, 0.01)
            lefty = int((-x*vy/vx)+y)
            righty = int(((cols-x)*vy/vx)+y)
            cv2.line(frame, (cols-1,righty), (0, lefty), (0, 255,0),2)
        except:
            pass
        
def odd_even(destination):
    for i in range(10):
        if (destination%2)==1:
            CARControl_UDP.Left(100)
        else:
            CARControl_UDP.Right(100)

#CARControl.setup()

ctrCmd = ["FF", "RR", "BB", "LL", "FR", "BR", "FL", "BL", "SS", "PP"]
cmd = []

HOST = ''
PORT = 8011
BUFSIZE = 1024
ADDR = (HOST,PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)

# 포트 설정
udpSerSock.bind(ADDR)
    
# 준비 완료 화면에 표시
print('udp echo server ready')

while True:
    print('Waiting for connection')
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    print('...connected from :', addr)
    try:
        while True:
            data = ''
            data = udpSerSock.recv(BUFSIZE)
            data = data.decode('utf-8')
            print(data)
            cmd = data.split(',')
            if cmd[0] == "joystick":
                if cmd[1] == ctrCmd[0]:
                    CARControl_UDP.Forward(int(cmd[2]))
                    print("Forward")
                elif cmd[1] == ctrCmd[1]:
                    CARControl_UDP.Right(int(cmd[2]))
                    print("Right")
                elif cmd[1] == ctrCmd[2]:
                    CARControl_UDP.Backward(int(cmd[2]))
                    print("Backward")
                elif cmd[1] == ctrCmd[3]:
                    CARControl_UDP.Left(int(cmd[2]))
                    print("Left")
                elif cmd[1] == ctrCmd[4]:
                    CARControl_UDP.F_Right(int(cmd[2]))
                    print("Forward Right")
                elif cmd[1] == ctrCmd[5]:
                    CARControl_UDP.B_Right(int(cmd[2]))
                    print("Backward Right")
                elif cmd[1] == ctrCmd[6]:
                    CARControl_UDP.F_Left(int(cmd[2]))
                    print("Forward Left")
                elif cmd[1] == ctrCmd[7]:
                    CARControl_UDP.B_Left(int(cmd[2]))
                    print("Backward Left")
                elif cmd[1] == ctrCmd[8]:
                    CARControl_UDP.Stop()
                    print("Stop")
                elif cmd[1] == ctrCmd[9]:
                    print("Poweroff")
                    CARControl_UDP.Poweroff()
                    break
                else:
                    break
            elif cmd[0] == "check":
                print("IP :", cmd[1])
            elif cmd[0] == "line":
                crossroad=0
                flag=0
                while True:
                    destination=int(cmd[1])
                    print("num :", cmd[1])
                    frame_list=[]# [center, left, right]
                    center = None
                    center_list=[None, None, None]
                    (_, frame) = camera.read()
                    for i in range(3):
                        frame_list.append(frame)
                        frame_list[i] = cv2.GaussianBlur(frame_list[i], (11, 11),1)
                        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                        mask = cv2.inRange(hsv, Color_Lower, Color_Upper)
                        if i==1:
                            cv2.rectangle(mask, (40,0),(320,240),(0,0,0),-1)
                        elif i==2:
                            cv2.rectangle(mask, (0,0),(280,240),(0,0,0),-1)
                        else:
                            cv2.rectangle(mask, (0,0),(320,120),(0,0,0),-1)
                            cv2.rectangle(mask, (0,0),(120,240),(0,0,0),-1)
                            cv2.rectangle(mask, (240,0),(320,240),(0,0,0),-1)
                        contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                        draw(contours, center_list, frame)
                    print(center_list)
                    
                    if center_list[0]!=None:
                        if center_list[0][0] > Frame_Width/2 + 20 :  #turnRight_Area Set
                            CARControl_UDP.Right(100)
                        elif center_list[0][0] < Frame_Width/2 -20 : #turnLeft_Area Set
                            CARControl_UDP.Left(100)
                        else:
                            if center_list[1]!=None and center_list[2]!=None :
                                if center_list[1][1] > Frame_Height/2 and center_list[2][1] > Frame_Height/2 :
                                    if flag==0:
                                        flag=1
                                        crossroad+=1
                                    else:
                                        if destination<3:
                                            if crossroad==1:
                                                odd_even(destination)
                                        elif destination<5:
                                            if crossroad==2:
                                                odd_even(destination)
                                        else:
                                            if crossroad==3:
                                                odd_even(destination)
                                else:
                                    flag=0
                            CARControl_UDP.Forward(100)
                            print("crossroad",crossroad)
                            print("flag", flag)
                    else:
                        CARControl_UDP.Stop()
                        print("break")
                        break
                    
                    cv2.imshow("Frame", frame)
                    key = cv2.waitKey(1) & 0xFF
    except KeyboardInterrupt:
        print("Terminated by Keborad Interrupt")
        GPIO.cleanup()
udpSerSock.close();


