#!/usr/bin/env python

import sys
import cfgInt
import cfgWANIP

'''
configure WAN IP and then configure LAN IP.
For detail, run ./<command.py>
'''

if __name__ == '__main__':
    cfgInt.checkPara()
    cfgWANIP.cfgWANIP(sys.argv[1]) 
    cfgInt.cfgInt(wanip = sys.argv[1], interface = sys.argv[2], zone = sys.argv[3], interfaceip = sys.argv[4])
