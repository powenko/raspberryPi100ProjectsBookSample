#!/usr/bin/env python
# author: Powen Ko
#!/usr/bin/python
from subprocess import *
import matplotlib
from  numpy import genfromtxt
matplotlib.use('Agg')
import pylab
import Image
import pygame
import os
import time
from time import strftime
#from pygame.locals import*
#from matplotlib.dates import DateFormatter
import RPi.GPIO as GPIO
import datetime
def run_cmd(cmd):
"""Used to run Linux commands"""
p = Popen(cmd, shell=True, stdout=PIPE)
output = p.communicate()[0]
return output
def ckyorn( prompt):
"""Used for Y/N prompt"""
while True:
a=raw_input( prompt + " [y,n,?]: " ).upper()
if a in [ 'Y', 'YES']:
return True
elif a in [ 'N', 'NO']:
return False
def delete_old_data():
""" Used to delete old data in input file. Will check for data older than 14 days
    and ask if you would like everything older than 7 days to be deleted. This should not being asked more than once a week"""
now = datetime.datetime.now()
#get the first line of the data file, which will be the oldest entry
getfirst = run_cmd("head -1 temperature_logging | awk '{print $2}'")
#convert string to time.
firstLineTime = datetime.datetime.strptime(getfirst, '%m-%d-%Y-%H:%M:%S ')
#Get the date and time for seven days ago from now.
sevenDaysAgo = now - datetime.timedelta(days=7)
sevenDaysAgoStr =  sevenDaysAgo.strftime('%m-%d-%Y-%T')
#If the data and time in the first line is older than 14 days, ask if okay to delete.
if (now - firstLineTime) > datetime.timedelta(days=14):
print ("More than 14 days worth of data has been collected.")
if ckyorn ("Would you like to delete data older than 7 days?"):
sedCommand = "sed -n -i  '/" + sevenDaysAgoStr[1:15] + "/,$p' temperature_logging"
run_cmd(sedCommand)
def displayText(text, size, line, color, clearScreen):
"""Used to display text to the screen. displayText is only configured to display
    two lines on the TFT. Only clear screen when writing the first line"""
if clearScreen:
screen.fill((0, 0, 0))
font = pygame.font.Font(None, size)
text = font.render(text, 0, color)
textRotated = pygame.transform.rotate(text, -90)
textpos = textRotated.get_rect()
textpos.centery = 80
if line == 1:
textpos.centerx = 90
screen.blit(textRotated,textpos)
elif line == 2:
textpos.centerx = 40
screen.blit(textRotated,textpos)
def displayTime():
"""Used to display date and time on the TFT"""
screen.fill((0, 0, 0))
font = pygame.font.Font(None, 50)
now=time.localtime()
for setting in [("%H:%M:%S",60),("%d  %b",10)] :
timeformat,dim=setting
currentTimeLine = strftime(timeformat, now)
text = font.render(currentTimeLine, 0, (0,250,150))
Surf = pygame.transform.rotate(text, -90)
screen.blit(Surf,(dim,20))
def graph(toKeep):
"""Used to display the graphs. Text will be shown before hand as
    the graphs take time to generate"""
global firstTime
imageFile = 'gp.png'
#Display some text stating that graphs are being generated
if toKeep == TwelveHours:
displayText('Creating', 35, 1,(200,200,1),True)
displayText('12 Hour Graph', 32, 2,(150,150,255), False)
elif toKeep == TwentyFourHours:
displayText('Creating', 35, 1,(200,200,1), True)
displayText('24 Hour Graph', 32, 2,(150,150,255), False)
elif toKeep == OneWeek:
displayText('Creating', 35, 1,(200,200,1), True)
displayText('One Week Graph', 28, 2,(150,150,255), False)
pygame.display.flip()
#Get temperature and time data from data file
temp = genfromtxt(dataFile, dtype=None, usecols=(0), skip_header = lines - toKeep)
timecaptured = genfromtxt(dataFile, dtype=None, usecols=(1), skip_header = lines - toKeep)
#Site the size of the font for the axis
for label in ax.get_xticklabels():
label.set_fontsize(8)
for label in ax.get_yticklabels():
label.set_fontsize(8)
#Create xaxis labels and only show every 12th or 96th
xlabels = range(toKeep)
if toKeep == OneWeek:
pylab.xticks(xlabels[::96], [v[:5:] for v in timecaptured[::96]])
else:
pylab.xticks(xlabels[::12], [v[11:16] for v in timecaptured[::12]])
#Plot the graph
pylab.plot(temp,linewidth=2, antialiased=True)
#Change some colours
ax.patch.set_facecolor('#FFFFCC')
ax.patch.set_alpha(0.5)
#Rotate the text in the xaxis
fig.autofmt_xdate(rotation=90)
#    ax.xaxis.set_major_formatter( DateFormatter('%H:%M') )
#Set the yaxsis limits
pylab.ylim(0,40)
#Save the graph as an image and the re-open it, rotate it and then display to TFT.
pylab.savefig(imageFile, facecolor=fig.get_facecolor(),bbox_inches='tight', dpi=80,pad_inches=0.03)
pil_im = Image.open(imageFile)
pil_out = pil_im.rotate(-90)
pil_out.save(imageFile)
img = pygame.image.load(imageFile)
screen.blit(img,(0,0))
pygame.display.flip()
#Clear graph data in preparation for next plot
pylab.cla()
#Reset the firstTime Variable
firstTime = 0
def main():
global ax,fig,screen
global firstTime,lines
global TwentyFourHours,TwelveHours,OneWeek
global dataFile
dataFile = 'temperature_logging'
size = width, height = 128, 160
TFTxSize = 2.28
TFTySize = 1.63
TwentyFourHours = 288
TwelveHours = 144
OneWeek = 2016
firstTime = True        #Used to work out if a function has already been run
whatToDisplay = 1       #What do display on screen
rotate = 1              #Used when automatically rotating the display.
startTime = time.time() #Used to work out how much time has passed when rotating.
#Set the framebuffer device to be the TFT
os.environ["SDL_FBDEV"] = "/dev/fb1"
#Setup pygame display
pygame.init()
pygame.mouse.set_visible(0)
screen = pygame.display.set_mode(size)
#Setup plot area
fig = pylab.figure()
ax = fig.add_subplot(111)
fig.set_size_inches(TFTxSize, TFTySize)
background = pygame.Surface(screen.get_size())
background = background.convert()
#Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN) #Read GPIO 17 as input
#Open data file and count how many lines
file = open(dataFile)
lines = sum(1 for word in file if "." in word)
file.seek(0,0)
delete_old_data()
while True:
time.sleep(.5)
"""Check to see if button is pressed, and if so, increment by  one
    or reset to one if over 6"""
if GPIO.input(17):
whatToDisplay = 1+(whatToDisplay%7) #Rotate between 1 and 6
firstTime = True      #If button pressed, set this to True
if whatToDisplay == 1:    #Display time
displayTime()
elif whatToDisplay == 2:  #Display last temperature recorded.
file.seek(-26,2)      #Go to end of data file to get temperature
currentTemp = file.readline(5) + ' \xb0C'
displayText('Current Temp', 30, 1, (200,200,1), True )
displayText(currentTemp, 50, 2, (150,150,255), False )
elif  whatToDisplay == 4 and firstTime:
graph(TwelveHours)
elif  whatToDisplay  == 5 and firstTime:
graph(TwentyFourHours)
elif  whatToDisplay == 6 and firstTime:
graph(OneWeek)
elif  whatToDisplay == 3:   #Rotate display
elapsedTime = time.time() - startTime
if elapsedTime > 5:
rotate = not rotate
startTime = time.time()
if rotate:
file.seek(-26,2)
currentTemp = file.readline(5) + ' \xb0C'
displayText('Current Temp', 30, 1, (200,200,1), True )
displayText(currentTemp, 50, 2, (150,150,255), False )




elif not rotate:
displayTime()
#Write to TFT
pygame.display.flip()
if __name__ == '__main__':
main()