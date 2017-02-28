#!/bin/bash

if [ ${#} -ne 1 ]; then
    echo "./command IP, e.g. ./command 10.0.0.20"
    exit
fi

./cfgWANIP.py ${1}
./cfgItfIP.py ${1} X2 LAN 192.168.10.1
./addLDAP.py ${1} 192.168.10.10 Administrator cdpQa123 shssoqa1.com
./addSSO.py ${1} 192.168.10.10 123456
./addTSA.py ${1} 192.168.10.10 123456
