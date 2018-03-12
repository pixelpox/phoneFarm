#!/usr/bin/python
import sys
import os
import Image
import pytesseract

if len(sys.argv) < 5:
        print("I need a serial number and LTRB cords")
        sys.exit()

deviceSerialNumber = sys.argv[1]
cropL = sys.argv[2]
cropT = sys.argv[3]
cropR = sys.argv[4]
cropB = sys.argv[5]

tmpDir = 'tmp'

photo = Image.open(tmpDir + "/" + deviceSerialNumber + '-screen.png')

photo.crop((cropL , cropT , cropR , cropB)).save(tmpDir + "/" + deviceSerialNumber + "-cropped.png")

screenContents = pytesseract.image_to_string(Image.open(tmpDir + "/" + deviceSerialNumber + "-cropped.png"))

for line in screenContents.splitlines():
        if line == 'Are you still watching?':
                print line
                execfile('pin-test.py')
