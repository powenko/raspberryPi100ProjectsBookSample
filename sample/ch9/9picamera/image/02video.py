#   www.powenko.com
import time
import picamera
import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)

with picamera.PiCamera() as camera:
    camera.start_preview()
    #GPIO.wait_for_edge(17, GPIO.FALLING)
    camera.resolution = (640, 480)
    camera.start_recording('my_video.h264', inline_headers=False)
    #GPIO.wait_for_edge(17, GPIO.FALLING)
    camera.wait_recording(60)
    camera.stop_recording()
    camera.stop_preview()
