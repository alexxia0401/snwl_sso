#!/usr/bin/env python3

import re

tel = '021-654321'

result = re.match(r'(\d{3})\-(\d{3,8})', tel)
print('result.group(0):', result.group(0))
print('result.group(1):', result.group(1))
print('result.group(2):', result.group(2))
print('result.groups():', result.groups())
