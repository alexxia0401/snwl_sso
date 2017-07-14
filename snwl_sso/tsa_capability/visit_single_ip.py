#!/usr/bin/python3

import http.client
import socket
import time
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

page = 1
ip = '192.168.81.1'

while True:    
    if page >= 14000:
        page = 1
        
    class BindableHTTPHandler(urllib.request.HTTPHandler):
        def http_open(self, req):
            return self.do_open(BindableHTTPConnectionFactory(ip), req)
    
    # connection counts within 1 second
    for j in range(5):
        try:
            opener = urllib.request.build_opener(BindableHTTPHandler)
            url = "http://10.103.64.220/page%s.htm" % str(page)
            page += 1
            print(opener.open(url).read().decode())
            opener.close()
        except Exception as e:
            print('%s visit "%s" failed...' % (ip, url))
            print(e)
            continue   
    time.sleep(1) 
