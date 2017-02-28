#!/usr/bin/env python

'''This script could automatically add LDAP server and do some configuration, like reading OU info.
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
e.g. ./addLDAP.py 10.0.0.66 192.168.10.10 Administrator cdpQa123 shssoqa1.com'''

# check parameters
while True:
    if len(sys.argv) == 1:
        print usage
        sys.exit()
    elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print usage
        sys.exit()
    elif len(sys.argv) != 6: 
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
ldapIP = sys.argv[2]
user = sys.argv[3]
password = sys.argv[4]
domain = sys.argv[5]

child.expect("admin@[A-Z0-9]{12}>")
child.sendline("configure terminal")

index == child.expect(["\(yes/no\)\?", "config\([A-Z0-9]{12}\)#"])
if index == 0:
    child.sendline("yes")
else:
    pass

child.expect("config\([A-Z0-9]{12}\)#")
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
