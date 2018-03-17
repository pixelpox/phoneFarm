#!/usr/bin/python
import sys
import Image
import json

serialNumber = sys.argv[1]
print("serial Number: " + sys.argv[1]) 
photo = Image.open('screen.png')
w  , h = photo.size
res = str(w) + "x" + str(h)
print(res)

'''
data = json.load(open('devices.json'))

#print data
#print data["devices"][0]["serialNumber"]

device = {'serialNumber' : ' + serialNumber + ' , 'resolution' : ' + res + ' }
data["devices"].append(device)

print("new devices\n")
print data

with open('devices.json' , 'w') as outfile:
        json.dump(data , outfile)

'''