#!/usr/bin/env python
# author: Powen Ko
import time, RPi.GPIO as GPIO
import urllib


def fetch_thing(url, params, method):
    params = urllib.urlencode(params)
    if method=='POST':
        f = urllib.urlopen(url, params)
    else:
        f = urllib.urlopen(url+'?'+params)
    return (f.read(), f.code)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(22, GPIO.IN)

a0 = GPIO.input(7)
a1 = GPIO.input(11)
a2 = GPIO.input(12)
a3 = GPIO.input(13)
a4 = GPIO.input(15)
a5 = GPIO.input(16)
a6 = GPIO.input(18)
a7 = GPIO.input(22)
total=a0+(a1*2)+(a2*4)+(a3*8)+(a4*16)+(a5*32)+(a6*64)+(a7*128)
temp=total*5*1000/256/10;
print a7,a6,a5,a4,a3,a2,a1,a0,"[",total,"]","[C=",temp,"]"
content, response_code = fetch_thing(
                                     'http://127.0.0.1/gettemp.php',
                                     {'id': 1, 'temp': temp},
                                     'GET'
                                     )