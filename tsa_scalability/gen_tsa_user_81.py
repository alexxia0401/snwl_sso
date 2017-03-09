#!/usr/bin/env python

'''
Generate TSA users for TSA scalability test
csv format:
domain,user, e.g.:
test,user1
test,user2
...
'''

def gen_tsa_user(c, i, j):
    filename = 'static' + str(c) + '.csv'
    fp = open(filename,'w')
    while i <= j:
        fp.write('test,user%s\r\n' % str(i))
        i += 1

if __name__ == '__main__':
    a = 1
    b = 1
    c = 1000

    while a <= 9:
        gen_tsa_user(a, b, c)
        a += 1
        b += 1000
        c += 1000
