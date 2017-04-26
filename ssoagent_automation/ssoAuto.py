#!/usr/bin/python3

'''
This script uses JSON to communicate with SSO agent to configure SSO appliance.
Apply for SSO agent 4.1.x
Tested under Python 3.5.x
Author: Qing Xia
'''

import json
import urllib.request

class SSO(object):
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
        
        jdata = json.dumps(SSO.addSSOData)
        req = urllib.request.Request(self.url,
                                     jdata.encode('utf-8'),
                                     SSO.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        response.close()
        data = data.decode()
        #print(data)
        data = json.loads(data)
        if data['Message'] == 'success':
            return (True, data)
        else:
            return (False, data)
        #print('Adding SSO agent %s result: %s' % (ip, data['Message']))
        
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
        return data

    def showSSO(self, data):
        print('-' * 20)
        for i in data['MethodOutput']:
            print('IP:', i['Ip'])
            print('SharedKey:', i['SharedKey'])
            print('FriendlyName:', i['FriendlyName'])
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
        #print(data)
        data = json.loads(data)

        for i in data['MethodOutput']:
            if i['Ip'] == str(ip):
                index = i['Index']
        try:
            SSO.delSSOData['MethodInput']['Index'] = index
        except:
            return -1
            #print("Didn't find %s, abort delete operation." % ip)
        else:
            jdata = json.dumps(SSO.delSSOData)
            req = urllib.request.Request(self.url,
                                         jdata.encode('utf-8'),
                                         SSO.header)
            response = urllib.request.urlopen(req)
            data = response.read()
            response.close()
            data = data.decode()
            #print(data)
            data = json.loads(data)
            if data['Message'] == 'success':
                return (True, data)
            else:
                return (False, data)
            #print('Deleting SSO agent %s result: %s' % (ip, data['Message']))

class RemoteSSO(object):
    '''Add, Delete, Get Remote SSO Agents'''
    header = {'Content-Type': 'application/json'}

    addData = {
        "MethodInput": {
            "FriendlyName": "",
            "Index": 0,
            "Ip": "",
            "Port": -1
        },
        "MethodName": "AddRemoteAgent",
        "Stub": 1
    }
 
    getData = {
        "MethodInput": "",
        "MethodName": "GetRemoteAgentList",
        "Stub": 2
    }

    delData = {
        "MethodInput": {
            "Index": -1
        },
        "MethodName": "RemoveRemoteAgent",
        "Stub": 3
    }
 
    def __init__(self, url):
        self.url = url

    def addRemoteSSO(self, ip, port, name):
        RemoteSSO.addData['MethodInput']['Ip'] = str(ip)
        RemoteSSO.addData['MethodInput']['Port'] = port
        RemoteSSO.addData['MethodInput']['FriendlyName'] = str(name)
        jdata = json.dumps(RemoteSSO.addData)

        req = urllib.request.Request(self.url,
                                     jdata.encode('utf-8'),
                                     RemoteSSO.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        response.close()
        data = json.loads(data.decode())
        #print(data)
        if data['Message'] == 'success':
            return (True, data)
        else:
            return (False, data)
        
    def getRemoteSSO(self):
        jdata = json.dumps(RemoteSSO.getData)
        req = urllib.request.Request(self.url,
                                     jdata.encode('utf-8'),
                                     RemoteSSO.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        response.close()
        data = json.loads(data.decode())
        return data
        
    def showSSO(self, data):
        print('-' * 20)
        for i in data['MethodOutput']:
            print('IP:', i['Ip'])
            print('FriendlyName:', i['FriendlyName'])
            print('-' * 20)

    def delSSO(self, ip):
        jdata = json.dumps(RemoteSSO.getData)
        req = urllib.request.Request(self.url,
                                     jdata.encode('utf-8'),
                                     RemoteSSO.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        response.close()
        data = data.decode()
        #print(data)
        data = json.loads(data)

        for i in data['MethodOutput']:
            if i['Ip'] == str(ip):
                index = i['Index']
        try:
            RemoteSSO.delData['MethodInput']['Index'] = index
        except:
            return -1
        else:
            jdata = json.dumps(RemoteSSO.delData)
            req = urllib.request.Request(self.url,
                                         jdata.encode('utf-8'),
                                         RemoteSSO.header)
            response = urllib.request.urlopen(req)
            data = response.read()
            response.close()
            data = data.decode()
            #print(data)
            data = json.loads(data)
            if data['Message'] == 'success':
                return (True, data)
            else:
                return (False, data)


if __name__ == '__main__':
#    alexSSO = SSO('http://10.103.64.44:12348')
#    result = alexSSO.getSSO()
#    alexSSO.showSSO(result)
#    (result, data) = alexSSO.addSSO('6.6.7.8', '123456', 'test7')
#    if result == True:
#        print('adding successfully.')
#        #print(data)
#    alexSSO.showSSO(alexSSO.getSSO())

    #(result, data) = alexSSO.delSSO('6.6.7.8')
    #if result == 1:
    #    print('deleting successfully.')
    #alexSSO.showSSO(alexSSO.getSSO())

    rmtSSO = RemoteSSO('http://10.103.64.44:12348')
    #result, data = rmtSSO.addRemoteSSO('1.2.3.4', 2260, 'test1')
    #print(result, data)

    rmtSSO.showSSO((rmtSSO.getRemoteSSO()))
    rmtSSO.delSSO('1.2.3.4')
