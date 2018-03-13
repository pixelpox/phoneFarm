#!/usr/bin/python
import sys
import os


def pullImage(deviceSerialNumber):
	tmpDir = 'tmp'
	print deviceSerialNumber
	capCmd = 'adb -s {dSN} shell screencap -p /sdcard/{dSN}-screen.png'.format(dSN=deviceSerialNumber)
	pullCmd = 'adb -s {dSN} pull /sdcard/{dSN}-screen.png {tmp}/'.format(dSN=deviceSerialNumber , tmp=tmpDir)
	os.system(capCmd)
	os.system(pullCmd)