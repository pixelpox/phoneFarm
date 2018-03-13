import sys
import json

jsonData = open('devices.json').read()
data = json.loads(jsonData)
jsonCount = len(data['devices'])


sys.stdout.write("%s" % jsonCount)
sys.exit(0)
