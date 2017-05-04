#!/usr/bin/env python

'''
Generate TSA users for TSA scalability test
csv format:
domain,user, e.g.:
test,user1
test,user2
...
'''

def gen_tsa_user(fileCount, startUser, maxUser):
    filename = 'static' + str(fileCount) + '.csv'
    with open(filename,'w') as fp:
        while startUser <= maxUser:
            fp.write('test,user%s\r\n' % str(startUser))
            startUser += 1

if __name__ == '__main__':
    count = 1
    b = 10001
    c = 12500

    while count <= 9:
        gen_tsa_user(count, b, c)
        count += 1
        b += 10000
        c += 10000
