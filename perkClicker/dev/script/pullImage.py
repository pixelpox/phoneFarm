#!/usr/bin/python
import sys
import os


if len(sys.argv) < 2:
	print("I need a serial number")
	sys.exit()

deviceSerialNumber = sys.argv[1]
tmpDir = 'tmp'
print deviceSerialNumber
capCmd = 'adb -s {dSN} shell screencap -p /sdcard/{dSN}-screen.png'.format(dSN = deviceSerialNumber)
pullCmd ='adb -s {dSN} pull /sdcard/{dSN}-screen.png {tmp}/'.format(dSN = deviceSerialNumber , tmp = tmpDir)
os.system(capCmd)
os.system(pullCmd)

