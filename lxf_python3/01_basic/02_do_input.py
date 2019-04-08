#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

name = input("Please enter your name: ")
print("hello,", name)

# more ways to write
print("hello, %s" % name)
print("hello, {}".format(name))
print("{0}, {1}".format("hello", name))
