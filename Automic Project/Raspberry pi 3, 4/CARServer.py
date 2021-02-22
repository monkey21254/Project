# CARServer.py
import CARControl
from socket import *
from time import ctime
import RPi.GPIO as GPIO
import sys


#CARControl.setup()

ctrCmd = ["F", "R", "B", "L", "S", "P"]


HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
        print('Waiting for connection')
        tcpCliSock,addr = tcpSerSock.accept()
        print('...connected from :', addr)
        try:
                while True:
                    data = ''
                    data = tcpCliSock.recv(BUFSIZE)
                    data = data.decode('utf-8')
                    print(data)
                    if not data:
                        break
                    if data == ctrCmd[0]:
                        CARControl.Forward()
                        print("Forward")
                    if data == ctrCmd[1]:
                        CARControl.Right()
                        print("Right")
                    if data == ctrCmd[2]:
                        CARControl.Backward()
                        print("Backward")
                    if data == ctrCmd[3]:
                        CARControl.Left()
                        print("Left")
                    if data == ctrCmd[4]:
                        CARControl.Stop()
                        print("Stop")
                    if data == ctrCmd[5]:
                        print("Poweroff")
                        CARControl.Poweroff()
                        break
                        
                    
                        
        except KeyboardInterrupt:
            print("Terminated by Keborad Interrupt")
            GPIO.cleanup()
tcpSerSock.close();

