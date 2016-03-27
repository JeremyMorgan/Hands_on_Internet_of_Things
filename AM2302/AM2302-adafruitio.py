#!/usr/bin/python

import sys
import Adafruit_DHT
import urllib
import urllib2

aiokey = "[YOUR AIO KEY]"

headers = {
    'x-aio-key' : aiokey,
    'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

def getUrl( feed ):
	return "https://io.adafruit.com/api/feeds/" + feed + "/data"


sensor = Adafruit_DHT.AM2302
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    tempf = 9.0/5.0 * temperature + 32
    tempdata = urllib.urlencode({ 'value' : tempf })
    humdata = urllib.urlencode({ 'value' : humidity })
	
    req = urllib2.Request(getUrl('temperature'), tempdata, headers)
    req2 = urllib2.Request(getUrl('humidity'), humdata, headers)

    response = urllib2.urlopen(req)
    response = urllib2.urlopen(req2)

    print tempf, humidity
	
else:
	print 'Failed to get reading. Try again!'
	sys.exit(1)
