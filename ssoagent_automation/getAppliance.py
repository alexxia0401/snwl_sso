#!/usr/bin/python

import urllib2
import json

url = 'http://10.103.64.68:12348'
data = {"MethodInput":"","MethodName":"GetApplianceList","Stub":2}
header = {'Content-Type' : 'application/json'}

req = urllib2.Request(url, json.dumps(data), header)
response = urllib2.urlopen(req)
data = response.read()
print data
response.close()

data = json.loads(data)

ip = data['MethodOutput'][0]['Ip']
print 'IP is', ip
