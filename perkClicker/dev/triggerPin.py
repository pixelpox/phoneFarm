#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
import time

if len(sys.argv) < 2:
        print("I need a pin to send a signal")
        sys.exit()


phonePin = int(sys.argv[1])

GPIO.setmode(GPIO.BCM)


GPIO.setup(phonePin, GPIO.OUT)
GPIO.output(phonePin , 0) #set it to low
time.sleep(0.5)
GPIO.setup(phonePin, GPIO.IN)
time.sleep(0.5)
GPIO.setup(phonePin, GPIO.OUT)
GPIO.output(phonePin , 0) #set it to low
time.sleep(0.5)
GPIO.setup(phonePin, GPIO.IN)
print "pressed pin: " + phonePin
