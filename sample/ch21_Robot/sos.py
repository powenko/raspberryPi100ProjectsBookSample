#!/usr/bin/env python
# author: Powen Ko
import time, RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
p1 = GPIO.PWM(17,1)   # channel=17 frequency=1Hz
p1.start(0)

p1.ChangeDutyCycle(50)
p1.ChangeFrequency(1)
time.sleep(3);
p1.ChangeFrequency(1*2)
time.sleep(1.5);
p1.ChangeFrequency(1)
time.sleep(3);

p1.stop()
GPIO.cleanup()

