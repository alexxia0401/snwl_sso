#!/usr/bin/env python

def conf_ip():
    fp = open('conf_ip.bat', 'w')
    fp.write('netsh interface ipv4 set address name="Local Area Connection" source=static addr=192.168.90.2 mask=255.255.0.0 gataway=192.168.90.1 gwmetric=30\r\n')
    for i in range(3, 256):
        fp.write('netsh interface ipv4 add address name="Local Area Connection" addr=192.168.90.%s mask=255.255.0.0 gwmetric=30\r\n' % i)
    for i in range(0, 256):
        fp.write('netsh interface ipv4 add address name="Local Area Connection" addr=192.168.91.%s mask=255.255.0.0 gwmetric=30\r\n' % i)
    for i in range(0, 2):
        fp.write('netsh interface ipv4 add address name="Local Area Connection" addr=192.168.92.%s mask=255.255.0.0 gwmetric=30\r\n' % i)
    fp.close()

if __name__ == '__main__':
    conf_ip()
