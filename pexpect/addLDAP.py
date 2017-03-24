#!/usr/bin/python3

'''
This script could automatically add LDAP server and do some configuration, like reading OU info.
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
    print('''Usage: command wanip ldapServerIP ldapUser password domainName
e.g. ./addLDAP.py 10.0.0.24 192.168.10.10 Administrator cdpQa123 shssoqa1.com''')

def checkPara():
    '''check parameters'''
    while True:
        if len(sys.argv) == 1:
            usage()
            sys.exit()
        elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
            usage()
            sys.exit()
        elif len(sys.argv) != 6: 
            usage()
            sys.exit()
        else:
            break

def addLDAP(wanip, ldapIP, user, password, domain):
    #ssh login
    child = pexpect.spawn("ssh admin@%s" % wanip, encoding='utf-8')
    child.logfile = sys.stdout
    
    # first ssh login or not
    index = child.expect(["\(yes/no\)\?", "password:"])
    if index == 0:
        child.sendline("yes")
    elif index == 1:
        pass
    else:
        print("Program error! Exit.")
        sys.exit()
    
    child.sendline("password") 
    child.expect("admin@[A-Z0-9]{12}>")
    child.sendline("configure terminal")
    
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
    child.sendline("user ldap")
    
    child.expect("\(config-user-ldap\)#")
    child.sendline("no use-tls")
    
    child.expect("\[cancel\]:")
    child.sendline("yes")
    
    child.expect("\(config-user-ldap\)#")
    child.sendline("server %s" % ldapIP)
    
    child.expect("\(config-ldap-server\)#")
    child.sendline("port 389")
    
    child.expect("\(config-ldap-server\)#")
    child.sendline("bind name %s location %s/Users" % (user, domain))
    
    child.expect("\(config-ldap-server\)#")
    child.sendline("bind-password %s" % password)
    
    child.expect("\(config-ldap-server\)#")
    child.sendline("commit")
    time.sleep(1)
    
    child.expect("\(config-ldap-server\)#")
    child.sendline("exit")
    
    child.expect("\(config-user-ldap\)")
    child.sendline("directory")
    
    child.expect("\(config-ldap-directory\)#")
    child.sendline("primary-domain %s" % domain)
    
    child.expect("\(config-ldap-directory\)#")
    child.sendline("commit")
    time.sleep(1)
    
    child.expect("\(config-ldap-directory\)#")
    child.sendline("read-trees-from-server replace")
    time.sleep(8)
    
    child.close()

if __name__ == '__main__':
    checkPara()
    addLDAP(wanip = sys.argv[1], ldapIP = sys.argv[2], user = sys.argv[3], password = sys.argv[4], domain = sys.argv[5])
