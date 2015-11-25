#!/usr/bin/env python
# author: Powen Ko
from SimpleCV import Image, Display
from time import sleep
import urllib
url="http://www.powenko.com/webservice/barcode/?encode=UPC-A&bdata=120000000789&height=50&scale=2&bgcolor=%23FFFFff&color=%23000000&onlyimage=yes&file=&type=png&Genrate=Submit"
filename="out.jpg"
urllib.urlretrieve(url,filename)
Display1 = Display()
img = Image(filename)
img.save(Display1)  # 顯示在畫面上
while not Display1.isDone():
    sleep(1)
        






