#!/usr/bin/python
import subprocess
import sys
import json
configDir = 'config'
jsonData = open(configDir + '/' + 'devices.json').read()
data = json.loads(jsonData)
numOfDevices = len(data['devices'])
print numOfDevices
print data

for i in range(0 , numOfDevices):
	print i
	deviceSerialNumber = data['devices'][i]['serialNumber']
	cropL = data['devices'][i]['cropL']
	cropT = data['devices'][i]['cropT']
	cropR = data['devices'][i]['cropR']
	cropB = data['devices'][i]['cropB']
	devicePin = data['devices'][i]['pin']
	
	subprocess.call(['./script/pullImage.py' , deviceSerialNumber])
	subprocess.call(['./script/processImage.py' , str(deviceSerialNumber) , str(cropL) , str(cropT) , str(cropR) , str(cropB) , devicePin])
