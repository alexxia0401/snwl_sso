#!/usr/bin/python3

'''
This script configure interface zone and IP.
Written by: Alex (Qing) Xia
Version: 0.2
Date: 3/21/2017
This script needs WAN IP ssh enabled.
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
    print('''Usage: command WANIP interface zone interfaceIP
e.g. ./cfgItfIP.py 10.0.0.20 X2 LAN 192.168.10.1''')

def checkPara():
    '''check parameters'''
    while True:
        if len(sys.argv) == 1:
            usage()
            sys.exit()
        elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
            usage()
            sys.exit()
        elif len(sys.argv) != 5:
            usage()
            sys.exit()
        else:
            break

def cfgInt(wanip, interface, zone, interfaceip):
    '''configure interface IP, zone.'''
    #ssh login
    child = pexpect.spawnu('ssh admin@%s' % wanip)
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
    
    # start configuring
    
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
    child.sendline("ip %s netmask 255.255.255.0" % interfaceip)
    
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

if __name__ == '__main__':
    checkPara()
    cfgInt(wanip = sys.argv[1], interface = sys.argv[2], zone = sys.argv[3], interfaceip = sys.argv[4])
