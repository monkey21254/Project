# CARControl_UDP.py
import RPi.GPIO as GPIO
import time
import sys

t = 0.02

TRIG = 23
ECHO = 24

RIGHT_FORWARD = 20
RIGHT_BACKWARD = 16
RIGHT_PWM = 21
LEFT_FORWARD = 26
LEFT_BACKWARD = 19
LEFT_PWM = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

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

def getDistance():
    GPIO.output(TRIG, False)
    time.sleep(1)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance,2)

    return distance 
    
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
    
def Left(speed):
    rightMotor(1 ,0, speed)            
    leftMotor(0 ,0, 0)
    cmd_text = "LEFT"
    time.sleep(t)
    
def Right(speed):
    rightMotor(0 ,0, 0)            
    leftMotor(1 ,0, speed)
    cmd_text = "RIGHT"
    time.sleep(t)
    
def Forward(speed):
    rightMotor(1 ,0, speed)
    leftMotor(1 ,0, speed)
    cmd_text = "FORWARD"
    
def Backward(speed):
    rightMotor(0 ,1, speed)
    leftMotor(0 ,1, speed)
    cmd_text = "BACKWARD"
    
def F_Right(speed):
    rightMotor(1 ,0, speed//2)
    leftMotor(1 ,0, speed)
    time.sleep(t)
    
def B_Right(speed):
    rightMotor(0 ,1, speed//2)
    leftMotor(0 ,1, speed)
    
def F_Left(speed):
    rightMotor(1 ,0, speed)
    leftMotor(1 ,0, speed//2)
    
def B_Left(speed):
    rightMotor(0 ,1, speed)
    leftMotor(0 ,1, speed//2)

def Stop():
    rightMotor(0 ,0, 0)
    leftMotor(0 ,0, 0)
    
def Poweroff():
    RIGHT_MOTOR.stop()
    LEFT_MOTOR.stop()
    GPIO.cleanup()
    sys.exit()

def PrintDistance():
    distance_value = getDistance()
    if distance_value > 2 and distance_value < 400:
        print("Distance is {:.2f} cm".format(distance_value))

    
if __name__ == '__main__':
    #rightMotor(1 ,0, 60)
    #leftMotor(1 ,0, 60)
    #Poweroff()
    pass

