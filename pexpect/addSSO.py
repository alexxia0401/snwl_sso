#!/usr/bin/env python

'''This script could automatically add SSO agent and enable it.
Written by: Alex (Qing) Xia
Version: 0.1
Date: Oct 17th 2016
This script doesn't work if UTM is not in non-conf t mode.
'''

import pexpect
import time
import sys
import os

os.system("rm -f ~/.ssh/known_hosts")

usage = '''Usage: command WANIP SSOAgentIP sharedKey
e.g. ./addSSO.py 10.0.0.20 192.168.10.10 123456'''

# check parameters
while True:
    if len(sys.argv) == 1:
        print usage
        sys.exit()
    elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print usage
        sys.exit()
    elif len(sys.argv) != 4: 
        print usage
        sys.exit()
    else:
        break

#ssh login
wanip = sys.argv[1]
child = pexpect.spawn("ssh admin@%s" % wanip)
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
        print "Program error! Exit."
        sys.exit()


#configure SSO agent IP, enable this agent, enable SSO authentication.
ssoAgentIP = sys.argv[2]
ssoAgentKey = sys.argv[3]

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
