#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


GPIO.setup(18, GPIO.OUT)
GPIO.output(18 , 0) #set it to low
time.sleep(0.5)
GPIO.setup(18, GPIO.IN)
print "press"
time.sleep(0.5)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18 , 0) #set it to low
time.sleep(0.5)
GPIO.setup(18, GPIO.IN)
print "press"
