#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
import time


def triggerPin(phonePin):
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(phonePin, GPIO.OUT)
    GPIO.output(phonePin , 0)  # set it to low
    time.sleep(0.5)
    GPIO.setup(phonePin, GPIO.IN)
    time.sleep(0.5)
    GPIO.setup(phonePin, GPIO.OUT)
    GPIO.output(phonePin , 0)  # set it to low
    time.sleep(0.5)
    GPIO.setup(phonePin, GPIO.IN)
    print "pressed pin: " + str(phonePin)
