#!/usr/bin/env python3

import re

str = '021-654321'

re_compile = re.compile(r'(\d{3})\-(\d{3,8})')
print(re_compile.match(str).groups())
