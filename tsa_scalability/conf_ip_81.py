#!/usr/bin/python3

def conf_ip(c, ipRange):
    filename = 'conf_ip_' + str(c) + '.bat'
    with open(filename, 'w') as fp:
        fp.write('netsh interface ipv4 set address name="Local Area Connection" source=static addr=192.168.80.101 mask=255.255.0.0 gataway=192.168.80.1 gwmetric=30\r\n')
        for i in range(1, ipRange):
            fp.write('netsh interface ipv4 add address name="Local Area Connection" addr=192.168.%s.%s mask=255.255.0.0 gwmetric=30\r\n' % (c, i))

if __name__ == '__main__':
    for x in range(81, 90):
        conf_ip(x, 63)
