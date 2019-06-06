#!/usr/bin/env python3

import re

str = 'a b   c'
print(str.split(' '))

print(re.split(r'\s+', str))

str2 = 'a,b, c  d'
print(re.split(r'[\,\s]+', str2))

str3 = 'a,b;; c  d'
print(re.split(r'[\,\;\s]+', str3))
