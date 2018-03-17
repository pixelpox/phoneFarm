import json#
import random
import datetime


configDir = 'config'


def getTimes():
	jsonData = open(configDir + '/' + 'schedule.json').read()
	data = json.loads(jsonData)
	print data
	
	startTime = datetime.datetime.strptime(data['startTime'] , '%H:%M').time()
	endTime = datetime.datetime.strptime(data['endTime'] , '%H:%M').time()
	variance = data['variance']
	
	currentTime = datetime.datetime.now().time()
	print currentTime
	print startTime
	
	
	
	if currentTime > startTime and currentTime < endTime:
		print "its after " + str(startTime)
	
	
	
if __name__ == "__main__":
	getTimes()