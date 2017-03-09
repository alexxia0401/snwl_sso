#!/usr/local/bin/python

'''This script could automatically configure WAN IP after UTM is factory default booted.
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
    index = child.expect(["\(yes/no\)\?", "[pP]assword:"])
    if index == 0:
        child.sendline("yes")
        child.expect("[pP]assword:")
        child.sendline("password")
        break
    elif index == 1:
        child.sendline("password")
        break
    else:
        print "Program error! Exit."
        sys.exit()


#configure SSO agent IP, enable this agent, enable SSO authentication.
tsaAgentIP = sys.argv[2]
tsaAgentKey = sys.argv[3]

child.expect("admin@[A-Z0-9]{12}>")
child.sendline("configure terminal")

index == child.expect(["\(yes/no\)\?", "\[no\]:" , "config\([A-Z0-9]{12}\)#"])
if index == 0 or index == 1:
    child.sendline("yes")
else:
    pass

child.expect("config\([A-Z0-9]{12}\)#")
child.sendline("user sso")

child.expect("\(config-user-sso\)#")
child.sendline("terminal-services-agent %s" % tsaAgentIP)

child.expect("\(add-ts-agent\[%s\]\)#" % tsaAgentIP)
child.sendline("shared-key %s" % tsaAgentKey)

child.expect("\(add-ts-agent\[%s\]\)#" % tsaAgentIP)
child.sendline("enable")

child.expect("\(add-ts-agent\[%s\]\)#" % tsaAgentIP)
child.sendline("exit")

child.expect("\(config-user-sso\)#")
child.sendline("method ts-agent")

child.expect("\(config-user-sso\)#")
child.sendline("commit")

time.sleep(2)
child.close()
