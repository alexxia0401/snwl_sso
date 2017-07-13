#!/usr/bin/python3

import http.client
import socket
import time
import threading
import urllib.request

class BindableHTTPConnection(http.client.HTTPConnection):
    def connect(self):
        """Connect to the host and port specified in __init__."""
        self.sock = socket.socket()
        self.sock.bind((self.source_ip, 0))
        if isinstance(self.timeout, float):
            self.sock.settimeout(self.timeout)
        self.sock.connect((self.host,self.port))

def BindableHTTPConnectionFactory(source_ip):
    def _get(host, port=None, strict=None, timeout=0):
        bhc=BindableHTTPConnection(host, port=port, timeout=timeout)
        bhc.source_ip=source_ip
        return bhc
    return _get

def visit(page, ip):
    class BindableHTTPHandler(urllib.request.HTTPHandler):
        def http_open(self, req):
            return self.do_open(BindableHTTPConnectionFactory(ip), req)
    
    try:
        opener = urllib.request.build_opener(BindableHTTPHandler)
        url = "http://10.103.64.220/page%s.htm" % str(page)
        print(opener.open(url).read().decode())
        opener.close()
    except Exception as e:
        print('%s visit %s failed...' % (ip, url))
        print(e)

d = 1
ip = '192.168.81.%s' % str(d)
page = 1

threads = []

for i in range(1, 256):
    n = "t%s = threading.Thread(target=visit, args=(%s, '%s'))" % (str(i), str(page), ip)
    #print n
    exec(n)
    d += 1
    ip = '192.168.81.%s' % str(d)
    page += 1
    
    m = "threads.append(t%s)" % str(i)
    #print m
    exec(m)   

for t in threads:
    t.setDaemon(True)
    t.start()
    
t.join()
time.sleep(1)
