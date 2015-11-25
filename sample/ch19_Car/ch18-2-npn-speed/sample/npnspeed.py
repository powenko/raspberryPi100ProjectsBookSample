#!/usr/bin/env python
# author: Powen Ko
import time, RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

p1 = GPIO.PWM(4,1000)   # channel=4 frequency=1000Hz
p1.start(0)

while True:
    for dc in range (5,101,5):
        p1.ChangeDutyCycle(dc)
            time.sleep(0.2);




