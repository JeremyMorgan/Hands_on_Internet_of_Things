import RPi.GPIO as GPIO
import time

pin = 7
ourdelay = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

def activateLED():
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(ourdelay)
	GPIO.output(pin,GPIO.LOW)
	time.sleep(ourdelay)

for x in range(0,5):
	activateLED()


GPIO.cleanup()
