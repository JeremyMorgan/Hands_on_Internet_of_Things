#!/usr/bin/python

import sys
import Adafruit_DHT

sensor = Adafruit_DHT.AM2302
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

ourfile = open("output.txt", 'a')

if humidity is not None and temperature is not None:
	tempf = 9.0/5.0 * temperature + 32
	ourfile.write(str(tempf) + "," + str(humidity))
	ourfile.write("\n")
	print tempf, humidity
else:
	print 'Failed to get reading. Try again!'
	sys.exit(1)

ourfile.close()
