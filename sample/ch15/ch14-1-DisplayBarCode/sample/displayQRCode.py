#!/usr/bin/env python
# author: Powen Ko
from SimpleCV import Image, Display
from time import sleep
import urllib
url="https://chart.googleapis.com/chart?chs=150x150&cht=qr&chl=Hello%20world&choe=UTF-8"
filename="out.jpg"
urllib.urlretrieve(url,filename)
Display1 = Display()
img = Image(filename)
img.save(Display1)  # 顯示在畫面上
while not Display1.isDone():
    sleep(1)
        






