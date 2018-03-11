import json

#json=open('devices.json' , 'r')

#data = json.load(json)
#data = json.load(open('newjson.json'))
data = json.load(open('devices.json'))

#print data
print data["devices"][0]["serialNumber"]

device = "{'serialNumber' : '1234' , 'resolution' : '123x345'}"
data["devices"].append(device)

print("new devices\n")
print data

with open('devices.json' , 'w') as outfile:
	json.dump(data , outfile)
