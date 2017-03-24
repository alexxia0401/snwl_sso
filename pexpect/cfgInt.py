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
    child = pexpect.spawn('ssh admin@%s' % wanip, encoding='utf-8')
    child.logfile = sys.stdout
    
    # first ssh login or not
    index = child.expect(["\(yes/no\)\?", "admin@%s's password:" % wanip, "Password:"])
    if index == 0:
        child.sendline("yes")
    elif index == 1:
        pass
    elif index == 2:
        pass
    else:
        print("Program error! Exit.")
        sys.exit()
    
    # start configuring
    child.sendline("password")
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
