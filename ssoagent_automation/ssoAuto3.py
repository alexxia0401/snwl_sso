#!/usr/bin/python3

'''
This script uses JSON to communicate with SSO agent to configure SSO appliaces.
Apply for SSO agent 4.1.x
Tested under Python 3.5.x
Author: Qing Xia
Create Date: April 11th 2017
'''

import urllib.request
import json
import sys

class SSO:
    '''Implemented add, get, delete SSO agent'''
    header = {'Content-Type': 'application/json'}

    # JSON data
    addSSOData = {
        "MethodInput": {
            "FriendlyName": "",
            "Index": 0,
            "Ip": "",
            "Port": "",
            "SharedKey": ""
        },
        "MethodName": "AddAppliance",
        "Stub": 1
    }

    getSSOData = {
        "MethodInput": "",
        "MethodName": "GetApplianceList",
        "Stub": 2
    }

    updSSOData = ''

    delSSOData = {
        "MethodInput": {
            "Index": ""
        },
        "MethodName": "RemoveAppliance",
        "Stub": 4
    }

    def __init__(self, url):
        self.url = url

    def addSSO(self, ip, key, name, port=2258):
        SSO.addSSOData['MethodInput']['Ip'] = str(ip)
        SSO.addSSOData['MethodInput']['Port'] = port
        SSO.addSSOData['MethodInput']['FriendlyName'] = str(name)
        SSO.addSSOData['MethodInput']['SharedKey'] = str(key)
        #print SSO.addSSOData
        jdata = json.dumps(SSO.addSSOData)
        req = urllib.request.Request(self.url,
                                     jdata.encode('utf-8'),
                                     SSO.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        response.close()
        data = data.decode()
        #print data
        data = json.loads(data)
        print('Adding SSO agent %s result: %s' % (ip, data['Message']))
        
    def getSSO(self):
        jdata = json.dumps(SSO.getSSOData)
        req = urllib.request.Request(self.url,
                                     jdata.encode('utf-8'),
                                     SSO.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        response.close()
        data = data.decode()
        data = json.loads(data)

        print('-' * 20)
        for i in data['MethodOutput']:
            print('IP:', i['Ip'])
            print('SharedKey:', i['SharedKey'])
            print('FriendName:', i['FriendlyName'])
            print('-' * 20)

    def updSSO(self):
        pass

    def delSSO(self, ip):
        jdata = json.dumps(SSO.getSSOData)
        req = urllib.request.Request(self.url,
                                     jdata.encode('utf-8'),
                                     SSO.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        response.close()
        data = data.decode()
        #print data
        data = json.loads(data)

        for i in data['MethodOutput']:
            if i['Ip'] == str(ip):
                index = i['Index']
        #print index
        try:
            SSO.delSSOData['MethodInput']['Index'] = index
        except:
            print("Didn't find %s, abort delete operation." % ip)
        else:
            jdata = json.dumps(SSO.delSSOData)
            req = urllib.request.Request(self.url,
                                         jdata.encode('utf-8'),
                                         SSO.header)
            response = urllib.request.urlopen(req)
            data = response.read()
            response.close()
            data = data.decode()
            #print data
            data = json.loads(data)
            print('Deleting SSO agent %s result: %s' % (ip, data['Message']))

if __name__ == '__main__':
    alexSSO = SSO('http://10.103.64.44:12348')
    alexSSO.getSSO()
    #alexSSO.addSSO('6.6.7.8', '123456', 'test7')
    alexSSO.delSSO('6.6.7.8')
    alexSSO.getSSO()
