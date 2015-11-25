#!/usr/bin/env python
# author: Powen Ko

import wiringpi2 as wiringpi
from subprocess import call
import pygame, sys, os, time
from pygame.locals import *

os.environ["SDL_FBDEV"] = "/dev/fb1"
w=128
h=160
pygame.init()
# set up the window
DISPLAYSURF = pygame.display.set_mode((w,h), 0, 32)
pygame.mouse.set_visible(0)
pygame.display.set_caption('Drawing')


count=0
import os
for root, dirs, files in os.walk("/"):
    for file in files:
        if (file.endswith(".png")) or (file.endswith(".jpg")) or (file.endswith(".gif")) :
            count=count+1
            if count > 10 :
                exit()
            print os.path.join(root, file)
            DISPLAYSURF.fill((0,0,0))
            img=pygame.image.load(os.path.join(root, file))
            img=pygame.transform.scale(img, (w,h))
            DISPLAYSURF.blit(img,(0,0))
            pygame.display.update()
            time.sleep(1)



