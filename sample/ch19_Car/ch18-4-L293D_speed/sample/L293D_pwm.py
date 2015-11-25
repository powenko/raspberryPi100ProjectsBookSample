#!/usr/bin/env
#__author__ = "Powen Ko"
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD) # GPIO.BCM

MotorIN1 = 11 # 17
MotorIN2 = 12 # 18
MotorEN1 = 13 # 21

GPIO.setup(MotorIN1,GPIO.OUT)
GPIO.setup(MotorIN2,GPIO.OUT)
GPIO.setup(MotorEN1,GPIO.OUT)
p1 = GPIO.PWM(MotorEN1,250)   #  frequency=250Hz
p1.start(0)

print "Turning motor on Clockwise."
GPIO.output(MotorIN1,GPIO.HIGH)
GPIO.output(MotorIN2,GPIO.LOW)
for dc in range (0,101,5):     # for(dc=0;dc<101;dc++5)
    p1.ChangeDutyCycle(dc)
        sleep(1)


print "Turning motor on Counterclockwise."
GPIO.output(MotorIN1,GPIO.LOW)
GPIO.output(MotorIN2,GPIO.HIGH)
for dc in range (0,101,5):
    p1.ChangeDutyCycle(dc)
        sleep(1)

print "Stopping motor"
GPIO.output(MotorEN1,GPIO.LOW)         ＃ 關閉馬達的動作。
GPIO.cleanup()                         ＃離開程式前，先恢復GPIO的接腳。

