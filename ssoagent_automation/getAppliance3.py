#!/usr/bin/python3

import urllib.request
import json

url = 'http://10.103.64.44:12348'
data = {"MethodInput":"","MethodName":"GetApplianceList","Stub":2}
header = {'Content-Type' : 'application/json'}

data = json.dumps(data)
data = bytes(data, 'utf8')

req = urllib.request.Request(url, data, header)
response = urllib.request.urlopen(req)
data = response.read()
print(data)
response.close()

#data = json.loads(data)

#ip = data['MethodOutput'][0]['Ip']
#print('IP is', ip)
