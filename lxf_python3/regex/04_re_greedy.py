#!/usr/bin/env python3

import re

str = '120300'

result1 = re.match(r'^(\d+)(0*)$', str)
print(result1.groups())

result2 = re.match(r'^(\d+?)(0*)$', str)
print(result2.groups())
