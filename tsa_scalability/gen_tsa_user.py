#!/usr/bin/env python

'''
Generate TSA users for TSA scalability test
csv format:
domain,user, e.g.:
test,user1
test,user2
...
'''

def gen_tsa_user():
    fp = open('static.csv','w')
    for i in range(0,10000):
        fp.write('test,user%s\r\n' % str(i))

if __name__ == '__main__':
    gen_tsa_user()
