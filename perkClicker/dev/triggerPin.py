#!/usr/bin/python
import RPi.GPIO as GPIO
import time
phonePin=15
GPIO.setmode(GPIO.BCM)


GPIO.setup(phonePin, GPIO.OUT)
GPIO.output(phonePin , 0) #set it to low
time.sleep(0.5)
GPIO.setup(phonePin, GPIO.IN)
print "press"
time.sleep(0.5)
GPIO.setup(phonePin, GPIO.OUT)
GPIO.output(phonePin , 0) #set it to low
time.sleep(0.5)
GPIO.setup(phonePin, GPIO.IN)
print "press"
