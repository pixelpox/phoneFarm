#!/usr/bin/python
import sys
import os
import subprocess
import Image
import pytesseract

if len(sys.argv) < 6:
        print("I need a serial number , LTRB cords and pin number")
        sys.exit()

deviceSerialNumber = sys.argv[1]
cropL = int(sys.argv[2])
cropT = int(sys.argv[3])
cropR = int(sys.argv[4])
cropB = int(sys.argv[5])
devicePin = sys.argv[6]

tmpDir = 'tmp'

photo = Image.open(tmpDir + "/" + deviceSerialNumber + '-screen.png')

photo.crop((cropL , cropT , cropR , cropB)).save(tmpDir + "/" + deviceSerialNumber + "-cropped.png")

screenContents = pytesseract.image_to_string(Image.open(tmpDir + "/" + deviceSerialNumber + "-cropped.png"))

for line in screenContents.splitlines():
        if line == 'Are you still watching?':
		print("Trigger on pin : " + devicePin)
		subprocess.call(['./script/triggerPin.py' , devicePin])
	else:
		print("No action needed")

