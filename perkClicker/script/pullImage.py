#!/usr/bin/python
import sys
import os


def pullImage(deviceSerialNumber):
	tmpDir = 'tmp'
	print "Pulling image for : " + str(deviceSerialNumber)
	capCmd = 'adb -s {dSN} shell screencap -p /sdcard/{dSN}-screen.png'.format(dSN=deviceSerialNumber)
	pullCmd = 'adb -s {dSN} pull /sdcard/{dSN}-screen.png {tmp}/ >/dev/null 2>&1'.format(dSN=deviceSerialNumber , tmp=tmpDir)
	os.system(capCmd)
	os.system(pullCmd)