#!/usr/bin/python3

'''
This script could automatically add SSO agent and enable it.
Written by: Qing Xia
reference:
https://pexpect.readthedocs.io/en/latest/api/pexpect.html#handling-unicode
Tested on Ubuntu16.04 and Python3
'''

import argparse
import pexpect
import sys
import time


def checkPara():
    '''check input parameters'''
    usage = '''e.g. ./addSSO.py 10.0.0.20 192.168.10.10 123456'''
    parser = argparse.ArgumentParser(description=usage)
    parser.add_argument('wanip',
                        help='firewall WAN IP, need ssh to be enabled')
    parser.add_argument('ip', help='SSO agent IP')
    parser.add_argument('key',
                        help='SSO agent shared key',
                        default=123456,
                        nargs='?',
                        type=str)
    args = parser.parse_args()

    global wanIp
    global ip
    global key
    wanIp = args.wanip
    ip = args.ip
    key = args.key


def addSSO(wanip, ssoAgentIP, ssoAgentKey):
    # ssh login
    child = pexpect.spawn("ssh admin@%s" % wanip, encoding='utf-8')
    child.logfile = sys.stdout

    # first ssh login or not
    index = child.expect(["\(yes/no\)\?",
                          "admin@%s's password:" % wanip,
                          "Password:",
                          pexpect.TIMEOUT])
    if index == 0:
        child.sendline("yes")
    elif index == 1:
        pass
    elif index == 2:    # SM9800 6.2.1.4
        pass
    elif index == 3:
        print('No pattern matched!!!')
    else:
        print("Program error! Exit.")
        sys.exit()

    child.sendline("password")

    # configure SSO agent IP, enable this agent, enable SSO authentication.
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

    # child.expect("config\([A-Z0-9]{12}\)#")
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

    time.sleep(1)
    child.close()


if __name__ == '__main__':
    checkPara()
    addSSO(wanip=wanIp, ssoAgentIP=ip, ssoAgentKey=key)
