#!/usr/bin/env python

def conf_ip(c, ipRange):
    filename = 'conf_ip_del_' + str(c) + '.bat'
    with open(filename, 'w') as fp:
        for i in range(1, ipRange):
            fp.write('netsh interface ipv4 delete address name="Local Area Connection" addr=192.168.%s.%s\r\n' % (c, i))

if __name__ == '__main__':
    for x in range(81, 90):
        conf_ip(x, 63)
