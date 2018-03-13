#!/usr/bin/python
import sys
import os
import subprocess
import Image
import pytesseract


def processImage(deviceSerialNumber , coord):
    
    tmpDir = 'tmp'
    
    photo = Image.open(tmpDir + "/" + deviceSerialNumber + '-screen.png')
    
    photo.crop((coord[0] , coord[1] , coord[2] , coord[3])).save(tmpDir + "/" + deviceSerialNumber + "-cropped.png")
    
    screenContents = pytesseract.image_to_string(Image.open(tmpDir + "/" + deviceSerialNumber + "-cropped.png"))
    
    for line in screenContents.splitlines():
        if line == 'Are you still watching?':
    		return True
    	else:
    		return False