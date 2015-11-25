#!/usr/bin/env python
# author: Powen Ko
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO_ECHO = 24
print "IR Signal"
GPIO.setup(GPIO_ECHO,GPIO.IN)      #設定接腳

start=0
stop=0
while True:
    start = time.time()
        duringDown=start-stop;
    while GPIO.input(GPIO_ECHO)==0:
       start = time.time()
    
    while GPIO.input(GPIO_ECHO)==1:
        stop = time.time()
        
    #計算波型的時間
    duringUp = stop-start
    info = "Up:%7.f" % (duringUp  *100000) + ",Down:%7.f" % (duringDown*100000)
    print info
    if duringUp>0.1:
       print("------------------")
# 離開並恢復接腳
GPIO.cleanup()


