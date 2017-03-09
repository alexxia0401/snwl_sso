#!/usr/bin/env python

import urllib2, httplib, socket, time

class BindableHTTPConnection(httplib.HTTPConnection):
    def connect(self):
        """Connect to the host and port specified in __init__."""
        self.sock = socket.socket()
        self.sock.bind((self.source_ip, 0))
        if isinstance(self.timeout, float):
            self.sock.settimeout(self.timeout)
        self.sock.connect((self.host,self.port))

def BindableHTTPConnectionFactory(source_ip):
    def _get(host, port=None, strict=None, timeout=0):
        bhc=BindableHTTPConnection(host, port=port, strict=strict, timeout=timeout)
        bhc.source_ip=source_ip
        return bhc
    return _get

j = 1
while 1:
    for i in range(1, 63):
        ip = '192.168.81.' + str(i)
        if j >= 9000:
            j = 0
        url = "http://10.103.64.42/page" + str(j) + ".htm"
        class BindableHTTPHandler(urllib2.HTTPHandler):
            def http_open(self, req):
                return self.do_open(BindableHTTPConnectionFactory(ip), req)
        try:
            opener = urllib2.build_opener(BindableHTTPHandler)
            print opener.open(url).read()
            opener.close()
        except:
            print 'continue...'
            continue
        time.sleep(2) 
