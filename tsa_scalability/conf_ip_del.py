#!/usr/bin/python3

def conf_ip(c, ipRange):
    '''c means 3rd ip range, ipRange means 4th MAX ip range
    e..g conf_ip(1, 256) will generate 192.168.1.1 - 192.168.1.255'''
    filename = 'conf_ip_del_' + str(c) + '.bat'
    with open(filename, 'w') as fp:
        for i in range(1, ipRange):
            fp.write('netsh interface ipv4 delete address name="Local Area Connection" addr=192.168.%s.%s\r\n' % (c, i))

if __name__ == '__main__':
    for i in range(81, 90):
        conf_ip(i, 256)
