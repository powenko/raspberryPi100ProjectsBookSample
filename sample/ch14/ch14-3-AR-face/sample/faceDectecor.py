#!/usr/bin/env python
# author: Powen Ko
from SimpleCV import Image, Display
from time import sleep
Display1 = Display()
Image1 = Image("raspberrypi.png")
Image1.save(Display1)
while not Display1.isDone():
    sleep(1)