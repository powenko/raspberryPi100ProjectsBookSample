#!/usr/bin/env python
# author: Powen Ko
print __doc__
import time
import csv
from SimpleCV import Color, ColorCurve, Camera, Image, pg, np, cv
from SimpleCV.Display import Display
cam = Camera()
display = Display((800,600))
data = "None"
mydict = dict()
myfile = "barcode-list.csv"
while display.isNotDone():
    display.checkEvents()
    img = cam.getImage()
    img.drawRectangle(img.width/4,img.height/4,img.width/2,img.height/2,color=Color.RED,width=3)
      if display.mouseLeft:     #當用戶按下左鍵時
        img.drawText("reading barcode... wait",10,10)
        img.save(display)
        barcode = img.findBarcode()   #辨識條碼
        if barcode:
           print barcode
           data = str(barcode[0].data)   #取得條碼資料
           print data
           if mydict.has_key(data):
              mydict[data] = mydict[data] + 1
           else:
              mydict[data] = 1
                      
        elif display.mouseRight:     #當用戶按下右鍵時
           print "save to CVS"
           target= open( myfile, "wb" )
           wtr= csv.writer( target )  #儲存資料
           wtr.writerow( ["item","count"])
           for d in mydict.items():
               wtr.writerow(d)        #儲存資料
           target.close()
      img.drawText("Click to scan.",10,10,color=Color.RED)
      myItem = "Last item scanned: " + data
      img.drawText(myItem,10,30) #加上文字
      img.save(display) #畫面顯示

    


                      


