#!/usr/bin/env
#__author__ = "Powen Ko"
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD) # GPIO.BCM

MotorIN1 = 11 # 17
MotorIN2 = 12 # 18
MotorEN1 = 13 # 21

MotorIN3 = 15 # 22
MotorIN4 = 16 # 23
MotorEN2 = 18 # 24

GPIO.setup(MotorIN1,GPIO.OUT) #  設定6個輸出的接腳
GPIO.setup(MotorIN2,GPIO.OUT)
GPIO.setup(MotorEN1,GPIO.OUT)
GPIO.setup(MotorIN3,GPIO.OUT)
GPIO.setup(MotorIN4,GPIO.OUT)
GPIO.setup(MotorEN2,GPIO.OUT)

p1 = GPIO.PWM(MotorEN1,250)   #  PWM 的頻率=250Hz
p1.start(0)                   #  執行PWM
p2 = GPIO.PWM(MotorEN2,250)   #  PWM 的頻率=250Hz
p2.start(0)                   #  執行PWM

print "Turning motor on Clockwise."
GPIO.output(MotorIN1,GPIO.HIGH)
GPIO.output(MotorIN2,GPIO.LOW)
GPIO.output(MotorIN3,GPIO.HIGH)
GPIO.output(MotorIN4,GPIO.LOW)
for dc in range (0,101,5):    # 意思如C語言的 for(dc=0;dc<101;dc++5)
    p1.ChangeDutyCycle(dc)    # 調整 EN1 的pwm 比例
    p2.ChangeDutyCycle(dc)
    sleep(0.2)

print "Turning motor on Counterclockwise."  #逆時鐘的處理
GPIO.output(MotorIN1,GPIO.LOW)
GPIO.output(MotorIN2,GPIO.HIGH)
GPIO.output(MotorIN3,GPIO.LOW)
GPIO.output(MotorIN4,GPIO.HIGH)
for dc2 in range (0,101,5):
    p1.ChangeDutyCycle(dc2)
    p2.ChangeDutyCycle(dc2)
    sleep(0.2)

print "Stopping motor"         # 關閉馬達的動作。
GPIO.output(MotorEN1,GPIO.LOW)
GPIO.output(MotorEN2,GPIO.LOW)
GPIO.cleanup()                 # 離開程式前，先恢復GPIO的接腳。




