#!/usr/bin/python3

'''
This script uses JSON to communicate with SSO agent to configure SSO appliance.
Apply for SSO agent 4.1.x
Tested under Python 3.5.x
Creator: Qing Xia
Contributors:
Joy Xu: eDiretory
Bruce Chen: Exchange Server
Alina Liu: Domain Controller
'''

import json
import urllib.request

class SSO(object):
    '''Implemented add, get, delete SSO agent'''
    header = {'Content-Type': 'application/json'}
    stub = 1

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

    delSSOData = {
        "MethodInput": {
            "Index": ""
        },
        "MethodName": "RemoveAppliance",
        "Stub": 4
    }

    addDCData = {
        "MethodInput": {
            "FriendlyName": "",
            "Index": 0,
            "Ip": "",
            "UserName": "",
            "Passwd": "",
            "MonitorMethods":2,
            "EventPollingInterval":"",
            "SessionTablePollingInterval":10
        },
        "MethodName": "AddDC",
        "Stub": 1
    }

    getDCData = {
        "MethodInput": "",
        "MethodName": "GetDCList",
        "Stub": 2
    }

    delDCData = {
        "MethodInput": {
            "Index": ""
        },
        "MethodName": "RemoveDC",
        "Stub": 4
    }

    addESData = {       
        "MethodInput": {
	        "UserName":"",
            "Password":"",
            "FriendlyName": "",
            "MonitorMethod":1,
            "EventPollingInterval":5,
            "Index": 0,
            "Ip": ""
        },
        "MethodName": "AddExchangeServer",
        "Stub": 1
    }

    getESData = {
        "MethodInput": "",
        "MethodName": "GetExchangeServerList",
        "Stub": 2
    }

    delESData = {
        "MethodInput": {
            "Index": 1
        },
        "MethodName": "RemoveExchangeServer",
        "Stub": 3
    }

    addRmtSSOData = {
        "MethodInput": {
            "FriendlyName": "",
            "Index": 0,
            "Ip": "",
            "Port": -1
        },
        "MethodName": "AddRemoteAgent",
        "Stub": 1
    }
 
    getRmtSSOData = {
        "MethodInput": "",
        "MethodName": "GetRemoteAgentList",
        "Stub": 2
    }

    delRmtSSOData = {
        "MethodInput": {
            "Index": -1
        },
        "MethodName": "RemoveRemoteAgent",
        "Stub": 3
    }

    addEDirData = {
        "MethodInput": {
            "Ip": "", 
            "Port": -1, 
            "UserDN": "", 
            "Passwd": "", 
            "BaseDN": "", 
            "PollingInterval": 10, 
            "UsingSSL": 1
         }, 
        "MethodName": "AddeDirectory", 
        "Stub": 1
    }

    getEDirData = {
        "MethodInput": "", 
        "MethodName": "GeteDirectoryList", 
        "Stub": 2
    }

    delEDirData = {
        "MethodInput": {
            "Index": ""
        }, 
        "MethodName": "RemoveDirectory", 
        "Stub": 3
    }

    def __init__(self, url):
        self.url = url

    def addSSO(self, ip, key, name, port=2258):
        SSO.addSSOData['MethodInput']['Ip'] = str(ip)
        SSO.addSSOData['MethodInput']['Port'] = port
        SSO.addSSOData['MethodInput']['FriendlyName'] = str(name)
        SSO.addSSOData['MethodInput']['SharedKey'] = str(key)
        SSO.addSSOData['Stub'] = SSO.stub
        SSO.stub += 1
        
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
        
    def getSSO(self):
        SSO.getSSOData['Stub'] = SSO.stub
        SSO.stub += 1
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
            SSO.delSSOData['Stub'] = SSO.stub
            SSO.stub += 1
        except:
            return (-1, -1)
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

    def addDC(self, ip, friendlyName, userName, password, eventInterval=5):
        SSO.addDCData['MethodInput']['Ip'] = str(ip)
        SSO.addDCData['MethodInput']['FriendlyName'] = str(friendlyName)
        SSO.addDCData['MethodInput']['UserName'] = str(userName)
        SSO.addDCData['MethodInput']['Passwd'] = str(password) 
        SSO.addDCData['MethodInput']['EventPollingInterval'] = eventInterval 
        SSO.addDCData['Stub'] = SSO.stub
        SSO.stub += 1
        
        jdata = json.dumps(SSO.addDCData)
        req = urllib.request.Request(self.url,
                                     jdata.encode('utf-8'),
                                     SSO.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        response.close()
        data = json.loads(data.decode())
        #print(data)
        if data['Message'] == 'success':
            return (True, data)
        else:
            return (False, data)

    def getDC(self):
        SSO.getDCData['Stub'] = SSO.stub
        SSO.stub += 1
        jdata = json.dumps(SSO.getDCData)
        req = urllib.request.Request(self.url,
                                     jdata.encode('utf-8'),
                                     SSO.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        response.close()
        data = data.decode()
        data = json.loads(data)
        return data

    def showDC(self, data):
        print('-' * 20)
        for i in data['MethodOutput']:
            print('Host Address:', i['Ip'])
            print('Domain Name:', i['DomainName'])
            print('NetBIOS Name:', i['NetBIOSName'])
            print('Friendly Name:', i['FriendlyName'])
            print('Status:', i['Hint'])
            print('-' * 20)

    def delDC(self, ip):
        jdata = json.dumps(SSO.getDCData)
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
            SSO.delDCData['MethodInput']['Index'] = index
            SSO.delDCData['Stub'] = SSO.stub
            SSO.stub += 1
        except:
            return (-1, -1)
        else:
            jdata = json.dumps(SSO.delDCData)
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

    def addES(self, ip, friendlyname, username, password):
        SSO.addESData['MethodInput']['Ip'] = str(ip)
        SSO.addESData['MethodInput']['FriendlyName'] = str(friendlyname)
        SSO.addESData['MethodInput']['UserName'] = str(username)
        SSO.addESData['MethodInput']['Passwd'] = str(password)
        SSO.addESData['Stub'] = SSO.stub
        SSO.stub += 1

        jdata = json.dumps(SSO.addESData)

        req = urllib.request.Request(self.url,
                                     jdata.encode('utf-8'),
                                     SSO.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        response.close()
        data = json.loads(data.decode())

        if data['Message'] == 'success':
            return (True, data)
        else:
            return (False, data)

    def getES(self):
        SSO.getESData['Stub'] = SSO.stub
        SSO.stub += 1
        jdata = json.dumps(SSO.getESData)
        req = urllib.request.Request(self.url,
                                     jdata.encode('utf-8'),
                                     SSO.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        response.close()
        data = json.loads(data.decode())
        return data

    def showES(self, data):
        print('-' * 20)
        for i in data['MethodOutput']:
            print('IP:', i['Ip'])
            print('UserName:', i['UserName'])
            print('FriendlyName:', i['FriendlyName'])
            print('Status:',i['Hint'])
            print('-' * 20)

    def delES(self, ip):
        jdata = json.dumps(SSO.getESData)
        req = urllib.request.Request(self.url,
                                     jdata.encode('utf-8'),
                                     SSO.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        response.close()
        data = data.decode()
        data = json.loads(data)

        for i in data['MethodOutput']:
            if i['Ip'] == str(ip):
                index = i['Index']
        try:
            SSO.delESData['MethodInput']['Index'] = index
            SSO.delESData['Stub'] = SSO.stub
            SSO.stub += 1
        except:
            return -1
        else:
            jdata = json.dumps(SSO.delESData)
            req = urllib.request.Request(self.url,
                                         jdata.encode('utf-8'),
                                         SSO.header)
            response = urllib.request.urlopen(req)
            data = response.read()
            response.close()
            data = data.decode()
            data = json.loads(data)
            if data['Message'] == 'success':
                return (True, data)
            else:
                return (False, data)
 
 
    def addRmtSSO(self, ip, port, name):
        SSO.addRmtSSOData['MethodInput']['Ip'] = str(ip)
        SSO.addRmtSSOData['MethodInput']['Port'] = port
        SSO.addRmtSSOData['MethodInput']['FriendlyName'] = str(name)
        SSO.addRmtSSOData['Stub'] = SSO.stub
        SSO.stub += 1
        jdata = json.dumps(SSO.addRmtSSOData)

        req = urllib.request.Request(self.url,
                                     jdata.encode('utf-8'),
                                     SSO.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        response.close()
        data = json.loads(data.decode())
        #print(data)
        if data['Message'] == 'success':
            return (True, data)
        else:
            return (False, data)
        
    def getRmtSSO(self):
        SSO.getRmtSSOData['Stub'] = SSO.stub
        SSO.stub += 1
        jdata = json.dumps(SSO.getRmtSSOData)
        req = urllib.request.Request(self.url,
                                     jdata.encode('utf-8'),
                                     SSO.header)
        response = urllib.request.urlopen(req)
        data = response.read()
        response.close()
        data = json.loads(data.decode())
        return data
        
    def showRmtSSO(self, data):
        print('-' * 20)
        for i in data['MethodOutput']:
            print('IP:', i['Ip'])
            print('FriendlyName:', i['FriendlyName'])
            print('-' * 20)

    def delRmtSSO(self, ip):
        jdata = json.dumps(SSO.getRmtSSOData)
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
            SSO.delRmtSSOData['MethodInput']['Index'] = index
            SSO.delRmtSSOData['Stub'] = SSO.stub
            SSO.stub += 1
        except:
            return (-1, -1)
        else:
            jdata = json.dumps(SSO.delRmtSSOData)
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

    def getEDir(self):
        SSO.getEDirData['Stub'] = SSO.stub
        SSO.stub += 1
        req = urllib.request.Request(self.url)
        req.add_header('Content-Type', 'application/json')
        response = urllib.request.urlopen(req,
            json.dumps(SSO.getEDirData).encode('utf-8'))
        data = response.read().decode()
        response.close()
        data = json.loads(data)
        return data

    def addEDir(self, ip, userDN, pwd, baseDN, port=636):
        SSO.addEDirData["MethodInput"]["Ip"] = str(ip)
        SSO.addEDirData["MethodInput"]["Port"] = port
        SSO.addEDirData["MethodInput"]["UserDN"] = str(userDN)
        SSO.addEDirData["MethodInput"]["Passwd"] = str(pwd)
        SSO.addEDirData["MethodInput"]["BaseDN"] = str(baseDN)
        SSO.addEDirData['Stub'] = SSO.stub
        SSO.stub += 1
        
        req = urllib.request.Request(self.url)
        req.add_header('Content-Type', 'application/json')
        response = urllib.request.urlopen(req,
            json.dumps(SSO.addEDirData).encode('utf-8'))
        data = response.read().decode()
        response.close()
        data = json.loads(data)
        #print(data)
        if data['Message'] == 'success':
            return (True, data)
        else:
            return (False, data)
    
    def delEDir(self, ip):
        req = urllib.request.Request(self.url)
        req.add_header('Content-Type', 'application/json')
        response = urllib.request.urlopen(req,
            json.dumps(SSO.getEDirData).encode('utf-8'))
        
        data = response.read().decode()
        response.close()
        data = json.loads(data)
        for i in data["MethodOutput"]:
            if i["Ip"] == str(ip):
                index = i["Index"]
        try:
            SSO.delEDirData["MethodInput"]["Index"] = index
            SSO.delEDirData['Stub'] = SSO.stub
            SSO.stub += 1
        except:
            return (-1, -1)
        else:
            req = urllib.request.Request(self.url)
            req.add_header('Content-Type', 'application/json')
            response = urllib.request.urlopen(req,
                json.dumps(SSO.delEDirData).encode('utf-8'))
            
            data = response.read().decode()
            response.close()
            data = json.loads(data)
            #print(data)
            if data["Message"] == "success":
                return (True, data)
            else:
                return (False, data)

    def showEDir(self, data):
        print('-' * 20)
        for i in data["MethodOutput"]:
            print("Novell eDriectory server IP: %s" % i["Ip"])
            print("UserDN: %s" % i["UserDN"])
            print("BaseDN: %s" % i["BaseDN"])
            print ("Password: %s" % i["Passwd"])
            print('-' * 20)

# test functions
def testSSO():
    testSSO = SSO('http://10.103.64.44:12348')
    testSSO.addSSO('192.168.101.1', '123456', 'test SSO 1')
    testSSO.addSSO('192.168.101.2', '123456', 'test SSO 2')
    testSSO.showSSO(testSSO.getSSO())
    testSSO.delSSO('192.168.101.2')

def testDC():
    testDC = SSO('http://10.103.64.44:12348')
    testDC.addDC('192.168.102.1', 'DC test1',
        'qatest\\administrator','cdpQa123')
    testDC.addDC('192.168.102.2', 'DC test2',
        'qatest\\administrator','cdpQa123',10)
    testDC.showDC(testDC.getDC())
    testDC.delDC('192.168.102.2')

def testES():
    testES = SSO('http://10.103.64.44:12348')
    testES.addES('192.168.103.1', 'ES test 1', 'CHY\\test1', '123456')
    testES.addES('192.168.103.2', 'ES test 2', 'CHY\\test2', '123456')
    testES.showES(testES.getES())
    testES.delES('192.168.103.2')

def testEDir():
    testEDir = SSO('http://10.103.64.44:12348')
    testEDir.addEDir('192.168.104.1', 'CN=Admin,o=qa','123456','o=qa')
    testEDir.addEDir('192.168.104.2', 'CN=Admin,o=qa','123456','o=qa', 637)
    testEDir.showEDir(testEDir.getEDir())
    testEDir.delEDir('192.168.104.2')

def testRmtSSO():
    testRmtSSO = SSO('http://10.103.64.44:12348')
    testRmtSSO.addRmtSSO('192.168.105.1', 2260, 'test RmtSSO 1')
    testRmtSSO.addRmtSSO('192.168.105.2', 2260, 'test RmtSSO 2')
    testRmtSSO.showRmtSSO(testRmtSSO.getRmtSSO())
    testRmtSSO.delRmtSSO('192.168.105.2')


if __name__ == '__main__':
    #testSSO()
    #testDC()
    #testES()
    #testEDir()
    #testRmtSSO()
