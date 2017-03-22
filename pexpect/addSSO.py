#!/usr/bin/python3

'''
This script could automatically add SSO agent and enable it.
Written by: Alex (Qing) Xia
Version: 0.2
Date: 3/22/2017
This script doesn't work if UTM is not in non-conf t mode.
!!! Using python3 !!!
diff: child = pexpect.spawnu(command)
Tested on Ubuntu16.04

'''

import pexpect
import time
import sys
import os

os.system("rm -f ~/.ssh/known_hosts")

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
    child = pexpect.spawnu("ssh admin@%s" % wanip)
    child.logfile = sys.stdout
    
    # first ssh login or not
    while True:
        index = child.expect(["\(yes/no\)\?", "password:"])
        if index == 0:
            child.sendline("yes")
            child.expect("admin@%s's password:" % wanip)
            child.sendline("password")
            break
        elif index == 1:
            child.sendline("password")
            break
        else:
            print("Program error! Exit.")
            sys.exit()
    
    #configure SSO agent IP, enable this agent, enable SSO authentication.
    child.expect("admin@[A-Z0-9]{12}>")
    child.sendline("configure terminal")
    
    index == child.expect(["\(yes/no\)\?", "config\([A-Z0-9]{12}\)#"])
    if index == 0:
        child.sendline("yes")
    else:
        pass
    
    child.expect("config\([A-Z0-9]{12}\)#")
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
