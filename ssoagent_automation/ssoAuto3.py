#!/usr/bin/python3

'''
SSO configuraton automation script
Apply for SSO 4.1.x
Using Python 3.5.x
Author: Alex Xia
Date: April 11th 2017
Tested under Ubuntu 16.04
'''

import urllib.request
import json
import sys

class sso:
    '''Implement add, get, delete SSO agent'''
    header = {'Content-Type' : 'application/json'}

    # JSON data
    addSsoData = {"MethodInput":{"Index":0,"Ip":"","Port":'',"FriendlyName":"","SharedKey":""},"MethodName":"AddAppliance","Stub":1}
    getSsoData = {"MethodInput":"","MethodName":"GetApplianceList","Stub":2}
    updSsoData = ''
    delSsoData = {"MethodInput":{"Index":''},"MethodName":"RemoveAppliance","Stub":4}

    def __init__(self, url):
        self.url = url

    def addSSO(self, ip, key, name, port = 2258):
        sso.addSsoData['MethodInput']['Ip'] = str(ip)
        sso.addSsoData['MethodInput']['Port'] = port
        sso.addSsoData['MethodInput']['FriendlyName'] = str(name)
        sso.addSsoData['MethodInput']['SharedKey'] = str(key)
        #print sso.addSsoData
        jdata = json.dumps(sso.addSsoData)
        req = urllib.request.Request(self.url, jdata.encode('utf-8'), sso.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        data = data.decode()
        #print data
        data = json.loads(data)
        response.close()
        print('Adding SSO agent %s result: %s' % (ip, data['Message']))
        
    def getSSO(self):
        jdata = json.dumps(sso.getSsoData)
        req = urllib.request.Request(self.url, jdata.encode('utf-8'), sso.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        data = data.decode()
        data = json.loads(data)
        response.close()
        print('-' * 20)
        for i in data['MethodOutput']:
            print('IP:', i['Ip'])
            print('SharedKey:', i['SharedKey'])
            print('FriendName:', i['FriendlyName'])
            print('-' * 20)

    def updSSO(self):
        pass

    def delSSO(self, ip):
        jdata = json.dumps(sso.getSsoData)
        req = urllib.request.Request(self.url, jdata.encode('utf-8'), sso.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        data = data.decode()
        #print data
        data = json.loads(data)
        response.close()
        index = -1
        for i in data['MethodOutput']:
            if i['Ip'] == str(ip):
                index = i['Index']
        #print index
        # need to raise exception if index is null
        if index == -1:
            print("Didn't find appliance. Won't continue delete operation.")
            sys.exit()
            #raise Exception
        sso.delSsoData['MethodInput']['Index'] = index
        #print sso.delSsoData
        jdata = json.dumps(sso.delSsoData)
        req = urllib.request.Request(self.url, jdata.encode('utf-8'), sso.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        data = data.decode()
        #print data
        data = json.loads(data)
        response.close()
        print('Deleting SSO agent %s result: %s' % (ip, data['Message']))
        

if __name__ == '__main__':
    alexSSO = sso('http://10.103.64.44:12348')
    alexSSO.getSSO()
    #alexSSO.addSSO('6.6.7.8', '123456', 'test7')
    #alexSSO.delSSO('6.6.7.8')
