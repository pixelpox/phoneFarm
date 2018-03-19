#!/usr/bin/python
import subprocess
import sys
import json
import subprocess
from pullImage import pullImage
from processImage import processImage
from triggerPin import triggerPin
from tapScreen import adbTapScreen
#from pushbullet import pushMessage

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
	print('hello there im perk3')
	
	#set still watching to false. this will be flipped when true
	stillWatching = False
	deviceHitBox = []
	
	#Load config from the devices file
	jsonData = open(configDir + '/' + 'devices.json').read()
	data = json.loads(jsonData)
	numOfDevices = len(data['devices'])
	
	#select each device in turn and check if they are stuck on still watching
	for i in range(0 , numOfDevices):
		
		#assign all data to a variable 
		deviceSerialNumber = data['devices'][i]['serialNumber']
		screenCoords = [
			data['devices'][i]['cropL']
		, 	data['devices'][i]['cropT']
		, 	data['devices'][i]['cropR']
		, 	data['devices'][i]['cropB']
		]
		
		devicePin = int(data['devices'][i]['pin'])
		
		#hitbox and ipaddress are optional vars
		if 'hitBox' in data['devices'][i]:
			deviceHitBox = data['devices'][i]['hitBox']
			
		if 'ipAddress' in data['devices'][i]:
			deviceIpAddress = data['devices'][i]['ipAddress']
			deviceSerialNumber = deviceIpAddress
		
		
		deviceOnline = checkDeviceOnline(deviceSerialNumber)
		if(deviceOnline):
			print "Connected to :" + str(deviceSerialNumber)
			pullImage(deviceSerialNumber)
			stillWatching = processImage(deviceSerialNumber , screenCoords)
			print str(deviceSerialNumber) + " Still watching? : " +str(stillWatching)
		else:
			#send out an sos
			print deviceSerialNumber + " : OFFLINE"
			#pushMessage(str(deviceSerialNumber) + ' IS OFFLINE' , 'Farm master has lost connectivity to a phone')
			
		#check if hitbox has been set
		if stillWatching and len(deviceHitBox) != 0:
			print "array has stuff in it"
			adbTapScreen(deviceSerialNumber , deviceHitBox)
		
		
		
		#Check if still watching prompt is showing
		#if(stillWatching):
			
			#triggerPin(devicePin)


if __name__ == '__main__':
	main()
