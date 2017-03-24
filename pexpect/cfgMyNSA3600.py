#!/usr/bin/python3

import os
import cfgWANIP
import cfgInt
import addSSO
import addTSA
import addLDAP 

'''
configure WAN IP and then configure LAN IP.
For detail, run ./<command.py>
'''

if __name__ == '__main__':
    mywanip = '10.0.0.24'
    # ssh key changed, needs to remove old key.
    os.system("rm -f ~/.ssh/known_hosts")

    cfgWANIP.cfgWANIP(wanip = mywanip) 
    cfgInt.cfgInt(wanip = mywanip, interface = 'X2', zone = 'LAN', interfaceip = '192.168.10.10')
    addSSO.addSSO(wanip = mywanip, ssoAgentIP = '192.168.10.40', ssoAgentKey = '123456')
    addTSA.addTSA(wanip = mywanip, tsaAgentIP = '192.168.10.40', tsaAgentKey = '123456')
    addLDAP.addLDAP(wanip = mywanip, ldapIP = '192.168.10.10', user = 'Administrator', password = 'cdpQa123', domain = 'shssoqa1')
