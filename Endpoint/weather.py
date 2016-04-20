#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Can enable debug output by uncommenting:
#import logging
#logging.basicConfig(level=logging.DEBUG)

import Adafruit_BMP.BMP085 as BMP085
import Adafruit_DHT
import urllib
import urllib2
import json

# URL of Endpoint
url = "http://internet-of-things.jeremymorgan.com:5000/weather/api/v1/readings"

# BMP085 is actually BMP180
sensor = BMP085.BMP085()

#AM2302
sensor2 = Adafruit_DHT.DHT22

# pin for the AM2302
pin = 4

# Read from the BMP180 First
temp1 = sensor.read_temperature()
pressure = sensor.read_pressure()
sealevelpressure = sensor.read_sealevel_pressure()

# Read from the AM2302
humidity, temp2 = Adafruit_DHT.read_retry(sensor2, pin)
tempavg = (temp1 + temp2) / 2

# Assemble Data Packet to send
data = {
    'temp1': str(temp1),
    'temp2': str(temp2),
    'tempavg' : str(tempavg),
    'pressure': str(pressure),
    'sealevelpressure': str(sealevelpressure),
    'humidity': str(humidity)
}

headers = {
    'Connection': 'keep-alive',
    'Content-type': 'application/json; charset=UTF-8',
}

#urldata = urllib.urlencode(data)
urldata = json.dumps(data)

req = urllib2.Request(url, urldata, headers)
response = urllib2.urlopen(req)
the_page = response.read()
