#!/usr/bin/python
import requests
import json

API_KEY = 'o.Rfj6Y7C4tGvgMmeSBQ8FSIHNGu7gVG9h'

# Send a message to all your registered devices.
def pushMessage(title, body):
    data = {
        'type':'note', 
        'title':title,
        'body':body
        }
    resp = requests.post('https://api.pushbullet.com/api/pushes',data=data, auth=(API_KEY,''))

# Test the function:    
pushMessage("Error in farm", "It looks like a phone is having an issue, please check it out")
