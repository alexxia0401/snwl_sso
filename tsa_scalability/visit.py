#!/usr/bin/env python

import urllib2
import time

def visit_page():
    i = 1
    limit = 10001
    while i < limit:
        k = i
        for j in range(3):
            try:
                url = 'http://10.103.64.42/page' + str(k) + '.htm'
                httpconn = urllib2.urlopen(url)
                html = httpconn.read()
                print html
                httpconn.close()
            except:
                continue
            k += 1
        time.sleep(1)
        i += 3

if __name__ == '__main__':
    visit_page()
