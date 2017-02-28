#!/usr/bin/env python

'''
static.csv format:
#ip,domain\username
e.g.
192.168.0.0,alex\alex0
192.168.0.1,alex\alex1
'''

def gen_sso_static():
    fp = open('static.csv','w')
    b = 0
    c = 0
    d = 0
    user_count = 0
    while b < 7:
        while c < 256:
            while d < 256:
                fp.write('192.%s.%s.%s,alex\\alex%s\r\n' % (str(b), str(c), str(d), str(user_count)))
                user_count += 1
                d += 1
            c += 1
            d = 0
            if user_count % 63 == 0:
                break
        b += 1
        c = 0
    fp.close()

if __name__ == '__main__':
    gen_sso_static()
