#!/usr/bin/python
from xSlopeClass import xSlopeClass
import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)

try:
    while True:
        
        x = xSlopeClass()
        y = x.xSlope()
        z = int(round(math.radians(y)))
        v = -z
        
        GPIO.output(7,z)
	time.sleep(0.0015)
	GPIO.output(7,1)

	time.sleep(2)

except KeyboardInterrupt:
	GPIO.cleanup()

