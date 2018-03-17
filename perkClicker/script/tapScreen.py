#!/usr/bin/python
import sys
import RPi.GPIO as GPIO
import time
import random
import subprocess
import os


def adbTapScreen(deviceSerialNumber , deviceHitBox):
    #print "Im about to tap the screen"
    positionX = random.randrange(deviceHitBox[0] , deviceHitBox[1] , 30)
    positionY = random.randrange(deviceHitBox[2] , deviceHitBox[3] , 20)
    print str(positionX) + "x" + str(positionY)
    
    tapCmd = "adb -s " + deviceSerialNumber + " shell input tap " + str(positionX) + " " + str(positionY)
    
    print tapCmd
    os.system(tapCmd)