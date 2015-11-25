#!/usr/bin/env
#__author__ = "Powen Ko"
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1A = 16
Motor1B = 18
Motor1E = 22

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

print "Turning motor on Clockwise."
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)

sleep(5)

print "Turning motor on Counterclockwise."
GPIO.output(Motor1A,GPIO.HIGH )
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)

sleep(5)

print "Stopping motor"
GPIO.output(Motor1E,GPIO.LOW)

GPIO.cleanup()





