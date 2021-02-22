import cv2
import time
import CARControl_UDP_ver2 as motor
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

crossroad=0
flag=0
# destination=5

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
    if (destination%2)==1:
        motor.TurnLeft()
    else:
        motor.TurnRight()

def followLine(destination):
    while True:
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
                cv2.rectangle(mask, (60,0),(320,240),(0,0,0),-1)
            elif i==2:
                cv2.rectangle(mask, (0,0),(260,240),(0,0,0),-1)
            else:
                cv2.rectangle(mask, (0,0),(320,120),(0,0,0),-1)
                cv2.rectangle(mask, (0,0),(90,240),(0,0,0),-1)
                cv2.rectangle(mask, (230,0),(320,240),(0,0,0),-1)
            contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            draw(contours, center_list, frame)
        print(center_list)
        
        if center_list[0]!=None:
            if center_list[0][0] > Frame_Width/2 + 20 :  #turnRight_Area Set
                motor.TurnRight()
            elif center_list[0][0] < Frame_Width/2 -20 : #turnLeft_Area Set
                motor.TurnLeft()
            else:
                if center_list[1]!=None and center_list[2]!=None :
                    if center_list[1][1] > Frame_Height/2 and center_list[2][1] > Frame_Height/2 :
                        if flag==0:
                            flag=1
                            crossroad+=1
                        else:
                            if destination<3 and crossroad==1:
                                odd_even(destination)
                            elif destination<5 and crossroad==2:
                                odd_even(destination)
                            else:
                                if crossroad==3:
                                    odd_even(destination)
                    else:
                        flag=0
                motor.Forward(100, 100)
                print(crossroad)
                print(flag)
        else:
            motor.Stop()
        
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF


#motor.Poweroff()
camera.release()
cv2.destroyAllWindows()
