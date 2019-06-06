#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

str = '021-123456'

result = re.match(r'^\d{3}\-\d{5,8}$', str)

if result:
    print('passed')
else:
    print('failed')
