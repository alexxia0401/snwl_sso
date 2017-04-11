#!/usr/bin/python

'''
SSO configuraton automation
Apply for SSO 4.1
Using python2.7
Author: Alex Xia
Date: April 11th 2017
'''

import urllib2
import json
import sys

class sso:
    '''Implement add, get, delete SSO agent'''
    header = {'Content-Type' : 'application/json'}

    # JSON data
    addSSOdata = {"MethodInput":{"Index":0,"Ip":"","Port":'',"FriendlyName":"","SharedKey":""},"MethodName":"AddAppliance","Stub":1}
    getSSOdata = {"MethodInput":"","MethodName":"GetApplianceList","Stub":2}
    updSSOdata = ''
    delSSOdata = {"MethodInput":{"Index":''},"MethodName":"RemoveAppliance","Stub":4}

    def __init__(self, url):
        self.url = url

    def addSSO(self, ip, key, name, port = 2258):
        sso.addSSOdata['MethodInput']['Ip'] = str(ip)
        sso.addSSOdata['MethodInput']['Port'] = port
        sso.addSSOdata['MethodInput']['FriendlyName'] = str(name)
        sso.addSSOdata['MethodInput']['SharedKey'] = str(key)
        #print sso.addSSOdata
        req = urllib2.Request(self.url, json.dumps(sso.addSSOdata), sso.header)
        response = urllib2.urlopen(req)
        data = response.read()
        #print data
        data = json.loads(data)
        response.close()
        print data['Message']
        
    def getSSO(self):
        req = urllib2.Request(self.url, json.dumps(sso.getSSOdata), sso.header)
        response = urllib2.urlopen(req)
        data = response.read()
        #print data
        data = json.loads(data)
        response.close()
        for i in data['MethodOutput']:
            print 'IP is', i['Ip']
            print 'SharedKey is', i['SharedKey']
            print 'FriendName is', i['FriendlyName']
            print '-' * 10

    def updSSO(self):
        pass

    def delSSO(self, ip):
        req = urllib2.Request(self.url, json.dumps(sso.getSSOdata), sso.header)
        response = urllib2.urlopen(req)
        data = response.read()
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
            print "Didn't find appliance."
            sys.exit()
            #raise Exception
        sso.delSSOdata['MethodInput']['Index'] = index
        #print sso.delSSOdata
        req = urllib2.Request(self.url, json.dumps(sso.delSSOdata), sso.header)
        response = urllib2.urlopen(req)
        data = response.read()
        #print data
        data = json.loads(data)
        response.close()
        print 'result:', data['Message']
        

if __name__ == '__main__':
    alexSSO = sso('http://10.103.64.44:12348')
    alexSSO.getSSO()
    alexSSO.delSSO('2.3.4.5')
    #alexSSO.addSSO('5.6.7.8', '123456', 'test5', 2258)

