
#!/usr/bin/python
# create by Powen Ko, www.powenko.com
import sys, getopt
import urllib
import os
from xml.dom import minidom

WEATHER_URL = 'http://xml.weather.yahoo.com/forecastrss?u=c&w=%s'
WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'

def weather_for_zip(zip_code):
    url = WEATHER_URL % zip_code
    dom = minidom.parse(urllib.urlopen(url))
    forecasts = ""
    ycondition = dom.getElementsByTagNameNS(WEATHER_NS, 'condition')[0]
    n= ycondition.getAttribute('text')
    t= ycondition.getAttribute('temp')
    return n+" "+t+"C"
     


zipcode=2436704
if(len(sys.argv)>1):
    zipcode=sys.argv[1]

str1=weather_for_zip(zipcode)
print str1
str2='python ./lcdv2.py '
newstr=str2+"'"+str1+"'"
print newstr
os.system(newstr)
