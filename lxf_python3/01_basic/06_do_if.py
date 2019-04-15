#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

age = int(input('Please input your age: '))

if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
