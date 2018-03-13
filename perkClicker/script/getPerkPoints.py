#!/usr/bin/python
import subprocess
import sys
import json
import subprocess
from pullImage import pullImage
from processImage import processImage
from triggerPin import triggerPin

configDir = 'config'


def checkDeviceOnline(deviceSerialNumber):
	# print('checking if device is online')
	output = subprocess.check_output(['adb', 'devices' , '-l' ])
	deviceList = output.splitlines()
	# print deviceList
	for device in deviceList:
		serial = device.split(" ")
		if deviceSerialNumber == serial[0]:
			return True
		
	return False


def main():
	print('hello there im perk2')
	stillWatching = False
	jsonData = open(configDir + '/' + 'devices.json').read()
	data = json.loads(jsonData)
	numOfDevices = len(data['devices'])
	print numOfDevices
	print data
	
	for i in range(0 , numOfDevices):
		# print i
		
		deviceSerialNumber = data['devices'][i]['serialNumber']
		screenCoords = [
			data['devices'][i]['cropL']
		, 	data['devices'][i]['cropT']
		, 	data['devices'][i]['cropR']
		, 	data['devices'][i]['cropB']
		]
		
		devicePin = int(data['devices'][i]['pin'])
		
		deviceOnline = checkDeviceOnline(deviceSerialNumber)
		if(deviceOnline):
			print "going to do stuff"
			pullImage(deviceSerialNumber)
			stillWatching = processImage(deviceSerialNumber , screenCoords)
			
		if(stillWatching):
			triggerPin(devicePin)


if __name__ == '__main__':
	main()
