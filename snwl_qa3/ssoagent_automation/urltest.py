#!/usr/bin/python3

import urllib.request

response = urllib.request.urlopen('http://10.103.64.220/page1.htm')
html = response.read()
response.close()
print(html.decode())
