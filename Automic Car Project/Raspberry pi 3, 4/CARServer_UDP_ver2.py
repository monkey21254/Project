# CARServer_UDP_ver2.py
import CARControl_UDP_ver2
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
    for i in range(15):
        if (destination%2)==1:
            CARControl_UDP_ver2.TurnLeft()
        else:
            CARControl_UDP_ver2.TurnRight()


#CARControl.setup()

ctrCmd = ["F","B","S","P"]
cmd = []

HOST = ''
PORT = 8011
BUFSIZE = 1024
ADDR = (HOST,PORT)

# tcpSerSock = socket(AF_INET, SOCK_STREAM)
# tcpSerSock.bind(ADDR)
# tcpSerSock.listen(5)

# 소켓 생성 (UDP = SOCK_DGRAM, TCP = SOCK_STREAM)
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
                if len(cmd[2])>=3:
                    cmd[2]="100"
                if len(cmd[3])>=3:
                    cmd[3]="100"    
                if not data:
                    break
                if cmd[1] == ctrCmd[0]:
                    CARControl_UDP_ver2.Forward(int(cmd[2]), int(cmd[3]))
                    print("Forward")
                if cmd[1] == ctrCmd[1]:
                    CARControl_UDP_ver2.Backward(int(cmd[2]), int(cmd[3]))
                    print("Backward")
                if cmd[1] == ctrCmd[2]:
                    CARControl_UDP_ver2.Stop()
                    print("Stop")
                if cmd[1] == ctrCmd[3]:
                    print("Poweroff")
                    CARControl_UDP_ver2.Poweroff()
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
                            CARControl_UDP_ver2.TurnRight()
                        elif center_list[0][0] < Frame_Width/2 -20 : #turnLeft_Area Set
                            CARControl_UDP_ver2.TurnLeft()
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
                            CARControl_UDP_ver2.Forward()
                            print("crossroad",crossroad)
                            print("flag", flag)
                    else:
                        CARControl_UDP_ver2.Stop()
                        print("break")
                        break
                
            
#         camera.release()
#         cv2.destroyAllWindows()
                    
                                   
    except KeyboardInterrupt:
        print("Terminated by Keborad Interrupt")
        GPIO.cleanup()
#     finally:
#         #motor.Poweroff()
#         camera.release()
#         cv2.destroyAllWindows()

udpSerSock.close();
