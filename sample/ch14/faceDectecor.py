#!/usr/bin/env python
# author: Powen Ko
from SimpleCV import *
from time import sleep
myCamera = Camera(prop_set={'width':320, 'height': 240})
myDisplay = Display(resolution=(320, 240))
while not myDisplay.isDone():
   frame = myCamera.getImage()
   faces = frame.findHaarFeatures('face')
   if faces:
     for face in faces:
        print "Face at: " + str(face.coordinates())
        facelayer = DrawingLayer((frame.width,frame.height))
        w=face.width()
        h=face.height()
        print "x:"+str(w)+" y:"+str(h)
        facebox_dim = (w,h)
        facebox = facelayer.centeredRectangle(face.coordinates(),facebox_dim)
        frame.addDrawingLayer(facelayer)
        frame.applyLayers()
   else:
        print "No faces detected."
   frame.save(myDisplay)
   sleep(.1)