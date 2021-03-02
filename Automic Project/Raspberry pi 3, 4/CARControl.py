# CARControl.py
import RPi.GPIO as GPIO
import time
import sys

TRIG = 23
ECHO = 24

TRIG_R = 27
ECHO_R = 17

TRIG_L = 18
ECHO_L = 25

RIGHT_FORWARD = 16
RIGHT_BACKWARD = 20
RIGHT_PWM = 21
LEFT_FORWARD = 19
LEFT_BACKWARD = 26
LEFT_PWM = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.setup(TRIG_R, GPIO.OUT)
GPIO.setup(ECHO_R, GPIO.IN)

GPIO.setup(TRIG_L, GPIO.OUT)
GPIO.setup(ECHO_L, GPIO.IN)

GPIO.setup(RIGHT_FORWARD,GPIO.OUT)
GPIO.setup(RIGHT_BACKWARD,GPIO.OUT)
GPIO.setup(RIGHT_PWM,GPIO.OUT)
GPIO.output(RIGHT_PWM,0)
RIGHT_MOTOR = GPIO.PWM(RIGHT_PWM,100)
RIGHT_MOTOR.start(0)
RIGHT_MOTOR.ChangeDutyCycle(0)

GPIO.setup(LEFT_FORWARD,GPIO.OUT)
GPIO.setup(LEFT_BACKWARD,GPIO.OUT)
GPIO.setup(LEFT_PWM,GPIO.OUT)
GPIO.output(LEFT_PWM,0)
LEFT_MOTOR = GPIO.PWM(LEFT_PWM,100)
LEFT_MOTOR.start(0)
LEFT_MOTOR.ChangeDutyCycle(0)

# def setup():
#     GPIO.setmode(GPIO.BCM)
# 
#     GPIO.setup(TRIG, GPIO.OUT)
#     GPIO.setup(ECHO, GPIO.IN)
# 
#     GPIO.setup(TRIG_R, GPIO.OUT)
#     GPIO.setup(ECHO_R, GPIO.IN)
# 
#     GPIO.setup(TRIG_L, GPIO.OUT)
#     GPIO.setup(ECHO_L, GPIO.IN)
# 
#     GPIO.setup(RIGHT_FORWARD,GPIO.OUT)
#     GPIO.setup(RIGHT_BACKWARD,GPIO.OUT)
#     GPIO.setup(RIGHT_PWM,GPIO.OUT)
#     GPIO.output(RIGHT_PWM,0)
#     #RIGHT_MOTOR = GPIO.PWM(RIGHT_PWM,100)
#     RIGHT_MOTOR.start(0)
#     RIGHT_MOTOR.ChangeDutyCycle(0)
# 
#     GPIO.setup(LEFT_FORWARD,GPIO.OUT)
#     GPIO.setup(LEFT_BACKWARD,GPIO.OUT)
#     GPIO.setup(LEFT_PWM,GPIO.OUT)
#     GPIO.output(LEFT_PWM,0)
#     #LEFT_MOTOR = GPIO.PWM(LEFT_PWM,100)
#     LEFT_MOTOR.start(0)
#     LEFT_MOTOR.ChangeDutyCycle(0)
    
#RIGHT Motor control
def rightMotor(forward, backward, pwm):
    GPIO.output(RIGHT_FORWARD,forward)
    GPIO.output(RIGHT_BACKWARD,backward)
    RIGHT_MOTOR.ChangeDutyCycle(pwm)

#Left Motor control
def leftMotor(forward, backward, pwm):
    GPIO.output(LEFT_FORWARD,forward)
    GPIO.output(LEFT_BACKWARD,backward)
    LEFT_MOTOR.ChangeDutyCycle(pwm)
    
def Left():
    rightMotor(0 ,0, 0)            
    leftMotor(1 ,0, 60)
    cmd_text = "LEFT"
    
def Right():
    rightMotor(1 ,0, 60)            
    leftMotor(0 ,0, 0)
    cmd_text = "RIGHT"
    
def Forward():
    rightMotor(1 ,0, 60)
    leftMotor(1 ,0, 60)
    cmd_text = "FORWARD"
    
def Backward():
    rightMotor(0 ,1, 60)
    leftMotor(0 ,1, 60)
    cmd_text = "BACKWARD"

def Stop():
    rightMotor(0 ,0, 0)
    leftMotor(0 ,0, 0)
    
def Poweroff():
    RIGHT_MOTOR.stop()
    LEFT_MOTOR.stop()
    GPIO.cleanup()
    sys.exit()
    
    
if __name__ == '__main__':
    pass
