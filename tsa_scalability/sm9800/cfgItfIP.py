#!/usr/local/bin/python

'''This script configure interface zone and IP.
Written by: Alex (Qing) Xia
Version: 0.1
Date: Oct 26th 2016
This script needs WAN IP ssh enabled.
'''

import pexpect
import time
import sys
import os

os.system("rm -f ~/.ssh/known_hosts")

usage = '''Usage: command WANIP interface zone interfaceIP
e.g. ./cfgItfIP.py 10.0.0.20 X2 LAN 192.168.10.1'''

# check parameters
while True:
    if len(sys.argv) == 1:
        print usage
        sys.exit()
    elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print usage
        sys.exit()
    elif len(sys.argv) != 5:
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

# start configuring
interface = sys.argv[2]
zone = sys.argv[3]
interfaceIP = sys.argv[4]

child.expect("admin@[A-Z0-9]{12}>")
child.sendline("configure terminal")

index == child.expect(["\(yes/no\)\?", "config\([A-Z0-9]{12}\)#"])
if index == 0:
    child.sendline("yes")
else:
    pass

child.expect("config\([A-Z0-9]{12}\)#")
child.sendline("interface %s" % interface)

child.expect("\(edit-interface\[%s\]\)#" % interface)
child.sendline("ip-assignment %s static" % zone)

child.expect("\(edit-%s-static\[%s\]\)#" % (zone, interface))
child.sendline("ip %s netmask 255.255.255.0" % interfaceIP)

child.expect("\(edit-%s-static\[%s\]\)#" % (zone, interface))
child.sendline("exit")

child.expect("\(edit-interface\[%s\]\)#" % interface)
child.sendline("management https")

child.expect("\(edit-interface\[%s\]\)#" % interface)
child.sendline("management ping")

child.expect("\(edit-interface\[%s\]\)#" % interface)
child.sendline("commit")

time.sleep(2)
child.close()
