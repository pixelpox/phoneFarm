#!/usr/bin/python
import requests
import json
import sys



# Send a message to all your registered devices.
def pushMessage(title, body):
    confDir = '/home/pi/phoneFarm/perkClicker/config'
    configFile = open(confDir +'/'+'pushbulletApiToken.txt' , 'r')
    API_KEY = configFile.read()
    
    data = {
        'type':'note', 
        'title':title,
        'body':body
        }
    resp = requests.post('https://api.pushbullet.com/api/pushes',data=data, auth=(API_KEY,''))


sys.exit()


# Test the function:    
#pushMessage("Error in farm", "It looks like a phone is having an issue, please check it out")
