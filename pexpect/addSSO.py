#!/usr/bin/python3

'''
This script could automatically add SSO agent and enable it.
Written by: Alex (Qing) Xia
Version: 0.2
Date: 3/22/2017
This script doesn't work if UTM is not in non-conf t mode.
!!! Using python3 !!!
reference:
https://pexpect.readthedocs.io/en/latest/api/pexpect.html#handling-unicode
Tested on Ubuntu16.04
apt-get install python-pip3
pip3 install pexpect
'''

import pexpect
import time
import sys

def usage():
    print('''Usage: command WANIP SSOAgentIP sharedKey
e.g. ./addSSO.py 10.0.0.20 192.168.10.10 123456''')

def checkPara():
    '''check input parameters'''
    while True:
        if len(sys.argv) == 1:
            usage()
            sys.exit()
        elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
            usage()
            sys.exit()
        elif len(sys.argv) != 4: 
            usage()
            sys.exit()
        else:
            break

def addSSO(wanip, ssoAgentIP, ssoAgentKey):
    #ssh login
    child = pexpect.spawn("ssh admin@%s" % wanip, encoding='utf-8')
    child.logfile = sys.stdout
    
    # first ssh login or not
    index = child.expect(["\(yes/no\)\?", "admin@%s's password:" % wanip, pexpect.TIMEOUT])
    if index == 0:
        child.sendline("yes")
    elif index == 1:
        pass
    elif index == 2:
        print('No pattern matched!!!')
    else:
        print("Program error! Exit.")
        sys.exit()
    
    child.sendline("password")

    #configure SSO agent IP, enable this agent, enable SSO authentication.
    child.expect("admin@[A-Z0-9]{12}>")
    child.sendline("configure terminal")

    # override logged in admin user
    index2 = child.expect(["\[no\]:", "config\([A-Z0-9]{12}\)#", pexpect.TIMEOUT])
    if index2 == 0:
        child.sendline("yes")
    elif index2 == 1:
        pass
    elif index2 == 2:
        print('No pattern matched!!!')
    else:
        print('Wrong!!!')
    
    #child.expect("config\([A-Z0-9]{12}\)#")
    child.sendline("user sso")
    
    child.expect("\(config-user-sso\)#")
    child.sendline("agent %s" % ssoAgentIP)
    
    child.expect("\(add-sso-agent\[%s\]\)#" % ssoAgentIP)
    child.sendline("shared-key %s" % ssoAgentKey)
    
    child.expect("\(add-sso-agent\[%s\]\)#" % ssoAgentIP)
    child.sendline("enable")
    
    child.expect("\(add-sso-agent\[%s\]\)#" % ssoAgentIP)
    child.sendline("exit")
    
    child.expect("\(config-user-sso\)#")
    child.sendline("method sso-agent")
    
    child.expect("\(config-user-sso\)#")
    child.sendline("commit")
    
    time.sleep(2)
    child.close()

if __name__ == '__main__':
    checkPara()
    addSSO(wanip = sys.argv[1], ssoAgentIP = sys.argv[2], ssoAgentKey = sys.argv[3])
