#!/usr/bin/env python
# author: Powen Ko
from SimpleCV import *
from time import sleep
myCamera = Camera(prop_set={'width':320, 'height': 240})   # 指定網路攝影機的影像大小
myDisplay = Display(resolution=(320, 240)) # 抓取網路攝影機的影像
pic=Image("glasses.png")
mask2= pic.createBinaryMask(color1=(0,0,0), color2=(254,254,254))  # 重點：設定去背顏色
while not myDisplay.isDone():
  frame = myCamera.getImage()
  faces = frame.findHaarFeatures('face')  #  搜尋人臉
      if faces:
        for face in faces:
          print "Face at: " + str(face.coordinates())# 列印出人練臉的中心位置
          facelayer = DrawingLayer((frame.width,frame.height))  # 準備一個新的圖層
          w=face.width()
          h=face.height()
          print "x:"+str(w)+" y:"+str(h)
          facebox_dim = (w,h)
          facebox = facelayer.centeredRectangle(face.coordinates(), facebox_dim)# 畫出一個正方形
          frame.addDrawingLayer(facelayer)
          frame.applyLayers()           #  把圖層放回畫面上
          # 辨識 眼睛
          myFace = face.crop() # 取的臉部的影像
          eyes = myFace.findHaarFeatures('eye') #辨識 眼睛
          if eyes:
             for eye in eyes:
                 # 計算出眼鏡的位置
                 xf = face.x -(face.width()/2)
                 yf = face.y -(face.height()/2)
                 xm = eye.x -(eye.width()/2)
                 ym = eye.y -(eye.height()/2)
                 x1=pic.width
                 x1=x1/2
                 x2=eye.width()
                 x2=x2/2
                 xmust = xf+xm -x1+x2
                 ymust = yf+ym
                 print "Eye at: " + str(eye.coordinates())
                 frame = frame.blit(pic,pos=(xmust,ymust),mask = mask2)    #畫出眼鏡
                                                                              
      else:
        print "No faces detected."
  frame.save(myDisplay)   # 顯示在畫面上
  sleep(.1)




