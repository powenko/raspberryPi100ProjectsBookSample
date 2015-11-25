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
        if key=='q':
            funExit()
            exit()
            return
        elif key=='1':
            print('speed 1')
            funSpeed(100,100)
        elif key=='2':
            print('speed 2')
            funSpeed(70,70)
        elif key=='2':
            print('speed 3')
            funSpeed(20,20)
        elif key=='w':
            print('forward')                       ＃往前跑
            GPIO.output(MotorIN1,GPIO.HIGH)
            GPIO.output(MotorIN2,GPIO.LOW)
            GPIO.output(MotorIN3,GPIO.HIGH)
            GPIO.output(MotorIN4,GPIO.LOW)
            funSpeed(50,50)
        elif key=='x':                             ＃往後跑
            print('backward')
            GPIO.output(MotorIN1,GPIO.LOW)
            GPIO.output(MotorIN2,GPIO.HIGH)
            GPIO.output(MotorIN3,GPIO.LOW)
            GPIO.output(MotorIN4,GPIO.HIGH)
            funSpeed(50,50)
        elif key=='a':                             ＃往左跑
            print('left')
            GPIO.output(MotorIN1,GPIO.HIGH)
            GPIO.output(MotorIN2,GPIO.LOW)
            GPIO.output(MotorIN3,GPIO.LOW)
            GPIO.output(MotorIN4,GPIO.HIGH)
            funSpeed(50,50)
        elif key=='d':                             ＃往右跑
            print('right')
            GPIO.output(MotorIN1,GPIO.LOW)
            GPIO.output(MotorIN2,GPIO.HIGH)
            GPIO.output(MotorIN3,GPIO.HIGH)
            GPIO.output(MotorIN4,GPIO.LOW)
            funSpeed(50,50)
        elif key=='s':
            print('stop')
            funSpeed(0,0)
        else:
            print("key="+key)
    return


def funSpeed(i1,i2):
    dc1=i1
    dc2=i2
    p1.ChangeDutyCycle(dc1)
    p2.ChangeDutyCycle(dc2)


def funInit():
    GPIO.setmode(GPIO.BOARD)            #  設定6個輸出的接腳
    GPIO.setup(MotorIN1,GPIO.OUT)
    GPIO.setup(MotorIN2,GPIO.OUT)
    GPIO.setup(MotorEN1,GPIO.OUT)
    GPIO.setup(MotorIN3,GPIO.OUT)
    GPIO.setup(MotorIN4,GPIO.OUT)
    GPIO.setup(MotorEN2,GPIO.OUT)

def funExit():                          # 關閉馬達的動作。
    print "Stopping motor"
    GPIO.output(MotorEN1,GPIO.LOW)
    GPIO.output(MotorEN2,GPIO.LOW)
    GPIO.cleanup()


MotorIN1 = 11 # 17
MotorIN2 = 12 # 18
MotorEN1 = 13 # 21
MotorIN3 = 15 # 22
MotorIN4 = 16 # 23
MotorEN2 = 18 # 24

print("Press 'q' to exit")
print("'w'=forward,'x'=backward,'a'=left,'d'=right,'s'=stop")
print("'1','2','3' motor speed")
funInit()
p1 = GPIO.PWM(MotorEN1,250)    #  PWM 的頻率=250Hz
p1.start(0)
p2 = GPIO.PWM(MotorEN2,250)
p2.start(0)

kethread = KeyEventThread()
kethread.start()





