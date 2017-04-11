#!/usr/bin/python

'''A prototype using JSON to configure SSO agent 4.1'''

import urllib2
import json

data = {"MethodInput":"","MethodName":"GetApplianceList","Stub":2}

req = urllib2.Request('http://10.103.64.44:12348')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))
print response.read()
