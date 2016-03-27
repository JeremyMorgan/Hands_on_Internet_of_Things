#!/usr/bin/python

import sys
import Adafruit_DHT
import urllib2

url = "http://data.sparkfun.com/input/"
publickey = "[YOUR PUBLIC KEY]"
privatekey = "[YOUR PRIVATE KEY]"

sensor = Adafruit_DHT.AM2302
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    tempf = 9.0/5.0 * temperature + 32
    url_response = urllib2.urlopen(url + publickey + "?private_key=" + privatekey + "&humidity=" + str(humidity) + "&temp=" + str(tempf))
    print tempf, humidity

else:
    print 'Failed to get reading. Try again!'
    sys.exit(1)
