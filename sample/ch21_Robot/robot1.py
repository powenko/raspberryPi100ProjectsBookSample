#!/usr/bin/env
#__author__ = "Powen Ko"
import RPi.GPIO as GPIO
from time import sleep
import threading
import sys
import sys, tty, termios

def getch():                 # 鍵盤處理
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

class KeyEventThread(threading.Thread):  # 多執行序
    def run(self):
        print("thread");
        Fun()

def Fun():
    print("Fun")
    while True:
        key=getch()                     # 按鍵處理
        print(key)
        if key=='q':
            funExit()
            exit()
            return
        elif key=='w':
            funSpeed(160,-1)
        elif key=='s':
            funSpeed(80,-1)
        elif key=='x':
            funSpeed(10,-1)
        elif key=='e':
            funSpeed(-1,100)
        elif key=='d':
            funSpeed(-1,40)
        elif key=='c':
            funSpeed(-1,15)
        else:
            print("key="+key)
    time.sleep(0.5)
    return



def funSpeed(i1,i2):
    if i1>0:
        duty = float(i1) / 10.0 + 2.5
        p1.ChangeDutyCycle(duty)
    if i2>=0:
        duty = float(i2) / 10.0 + 2.5
        p2.ChangeDutyCycle(duty)



def funInit():
    GPIO.setmode(GPIO.BOARD)            #  設定2個輸出的接腳
    GPIO.setup(Motor1,GPIO.OUT)
    GPIO.setup(Motor2,GPIO.OUT)

def funExit():                          # 關閉馬達的動作。
    print "Stopping motor"
    GPIO.cleanup()


Motor1 = 11 # 17
Motor2 = 12 # 18


print("Press 'q' to exit")
print("'w','s','x'=left arm,  'e','d','c'=right arm ")
funInit()
p1 = GPIO.PWM(Motor1,100)    #  PWM 的頻率=250Hz
p1.start(0)
p2 = GPIO.PWM(Motor2,100)
p2.start(0)
funSpeed(20,20)


kethread = KeyEventThread()
kethread.start()





