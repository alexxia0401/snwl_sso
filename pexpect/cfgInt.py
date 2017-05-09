#!/usr/bin/python3

'''
This script configure interface zone and IP.
Written by: Alex (Qing) Xia
This script needs WAN IP ssh enabled.
Tested on Ubuntu16.04 and python3.5.x
'''

import argparse
import pexpect
import sys
import time

def checkPara():
    '''check input parameters'''
    usage='''e.g. ./cfgInt.py 10.0.0.20 X2 LAN 192.168.10.1'''
    parser = argparse.ArgumentParser(description=usage)
    parser.add_argument('wanip',
                        help='firewall WAN IP, need ssh to be enabled')
    parser.add_argument('interface',
                        help='interface you want to configure')
    parser.add_argument('zone',
                        help='zone you want to use')
    parser.add_argument('interfaceIP',
                        help='IP you want to give to interface')
    args = parser.parse_args()

    global wanIp
    global interface
    global zone
    global intIp
    wanIp  = args.wanip
    interface = args.interface
    zone = args.zone
    intIp = args.interfaceIP

def cfgInt(wanip, interface, zone, interfaceip):
    '''configure interface IP, zone.'''
    #ssh login
    child = pexpect.spawn('ssh admin@%s' % wanip, encoding='utf-8')
    child.logfile = sys.stdout
    
    # first ssh login or not
    index = child.expect(["\(yes/no\)\?",
        "admin@%s's password:" % wanip, "Password:"])
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
    index2 = child.expect(["\[no\]:",
        "config\([A-Z0-9]{12}\)#",
        pexpect.TIMEOUT])
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
    cfgInt(wanIp, interface, zone, intIp)
