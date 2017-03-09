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

#get port number
ipDict = {'10.0.0.66':'2029',
'10.0.0.25':'2011',
'10.0.0.20':'2043',
'10.0.0.61':'2022',
'10.0.0.64':'2025',
'10.0.0.67':'2026',
'10.0.0.68':'2027',
'10.7.70.93':'2016',
'10.7.70.94':'2042'}

usage = '''Usage: command WANIP
e.g. ./cfgWANIP.py 10.0.0.25'''

while True:
    if len(sys.argv) == 1:
        print usage
        sys.exit()
    elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print usage
        sys.exit()
    elif len(sys.argv) != 2:
        print usage
        sys.exit()
    else:
        break

#telnet login (console login)
wanip = sys.argv[1]
port = ipDict[wanip]

child = pexpect.spawn("telnet 10.103.64.8 %s" % port)
child.logfile = sys.stdout
child.expect("login:")
child.sendline("admin")
child.expect("Password:")
child.sendline("password")
time.sleep(1)
child.sendline("")

while True:
    index = child.expect(["User", "admin@[A-Z0-9]{12}>"])
    if index == 0:
        child.sendline("admin")
        child.expect("Password:")
        child.sendline("password")
        child.expect("admin@[A-Z0-9]{12}>")
        child.sendline("configure terminal")
        break
    elif index == 1:
        child.sendline("configure terminal")        
        break
    else:
        print "Program error! Exit."
        sys.exit()

# login to UTM console, starting to configure WAN IP
child.expect("config\([A-Z0-9]{12}\)#")
child.sendline("interface X1")

child.expect("\(edit-interface\[X1\]\)#")
child.sendline("ip-assignment WAN static")

child.expect("\(edit-WAN-static\[X1\]\)#")
child.sendline("ip %s netmask 255.255.255.0" % wanip)

child.expect("\(edit-WAN-static\[X1\]\)#")
child.sendline("gateway 10.0.0.1")

child.expect("\(edit-WAN-static\[X1\]\)#")
child.sendline("dns primary 10.217.131.101")

child.expect("\(edit-WAN-static\[X1\]\)#")
child.sendline("exit")

child.expect("\(edit-interface\[X1\]\)#")
child.sendline("management https")

child.expect("\(edit-interface\[X1\]\)#")
child.sendline("management ssh")

child.expect("\(edit-interface\[X1\]\)#")
child.sendline("management ping")

child.expect("\(edit-interface\[X1\]\)#")
child.sendline("commit")

time.sleep(2)
child.close()
