#!/usr/bin/python3

# Generate TSA users for TSA scalability test
# csv format:
# domain,user, e.g.:
# test,user1
# test,user2
# ...

def gen_tsa_user():
    with open('static.csv','w') as fp:
        for i in range(0,15000):
            n = str(i)
            fp.write('test,user%s\r\n' % n.zfill(5))

if __name__ == '__main__':
    gen_tsa_user()
