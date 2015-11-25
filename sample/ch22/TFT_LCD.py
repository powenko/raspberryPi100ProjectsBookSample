#!/usr/bin/env python
# author: Powen Ko
import wiringpi2 as wiringpi
from subprocess import call
import pygame, sys, os, time
from pygame.locals import *
os.environ["SDL_FBDEV"] = "/dev/fb1"


pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((128, 160), 0, 32)
pygame.mouse.set_visible(0)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# draw on the surface object
DISPLAYSURF.fill(BLACK)
print "black"
time.sleep(.5)
pygame.display.update()

DISPLAYSURF.fill(RED)
print "red"
time.sleep(.5)
pygame.display.update()

DISPLAYSURF.fill(GREEN)
print "green"
time.sleep(.5)
pygame.display.update()

DISPLAYSURF.fill(BLUE)
print "blue"
time.sleep(.5)
pygame.display.update()

DISPLAYSURF.fill(WHITE)
print "white"
time.sleep(.5)
pygame.display.update()

# demo draw some shapes
pygame.draw.polygon(DISPLAYSURF, GREEN, ((16, 0), (111, 106), (36, 277), (56, 27), (0, 106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (40, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (110, 200, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (100, 150, 100, 50))
pygame.display.update()
time.sleep(.5)


font = pygame.font.Font(None, 36)
text = font.render("powenko", 1, BLUE)
textpos = text.get_rect(centerx=DISPLAYSURF.get_width()/2)
DISPLAYSURF.blit(text, textpos)
pygame.display.update()
time.sleep(.5)







