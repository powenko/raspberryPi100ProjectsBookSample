#!/usr/bin/python
# create by Powen Ko, www.powenko.com
import sys, getopt
import urllib
from xml.dom import minidom

WEATHER_URL = 'http://xml.weather.yahoo.com/forecastrss?u=c&w=%s'
WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'

def weather_for_zip(zip_code):
    url = WEATHER_URL % zip_code
    dom = minidom.parse(urllib.urlopen(url))
    forecasts = []
    for node in dom.getElementsByTagNameNS(WEATHER_NS, 'forecast'):
        forecasts.append({
                         'date': node.getAttribute('date'),
                         'low': node.getAttribute('low'),
                         'high': node.getAttribute('high'),
                         'condition': node.getAttribute('text')
                         })
    ycondition = dom.getElementsByTagNameNS(WEATHER_NS, 'condition')[0]
    return {
        'current_condition': ycondition.getAttribute('text'),
        'current_temp': ycondition.getAttribute('temp'),
        'forecasts': forecasts,
        'title': dom.getElementsByTagName('title')[0].firstChild.data
}


zipcode=2436704
if(len(sys.argv)>0):
    zipcode=sys.argv[1]
print weather_for_zip(zipcode)