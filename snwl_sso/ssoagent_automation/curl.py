#!/usr/bin/python

'''
Need to install pycurl module first.
'''

import pycurl
import StringIO
import json

buf = StringIO.StringIO()

c = pycurl.Curl()
c.setopt(c.URL, 'http://10.103.64.44')
c.setopt(c.PORT, 12348)
c.setopt(c.POSTFIELDS, '{"MethodInput":"","MethodName":"GetApplianceList","Stub":2}') # post data, curl -d 'data'
c.setopt(c.HTTPHEADER, ['Content-Type: application/json']) # set http header
#c.setopt(c.VERBOSE, True)
c.setopt(c.WRITEFUNCTION, buf.write)
c.perform()

result = buf.getvalue()
buf.close()
print(result)

data = json.loads(result)
print data

print data['Stub']
print data['MethodOutput'][0]['SharedKey']
