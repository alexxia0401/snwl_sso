#!/usr/bin/env python3

# *args is tuple
def func1(arg, *args):
    print(arg, args)
    print(type(args))

func1(1, 2, 3, 4, 5)

# **kwargs is dictionary
def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))

func2(a=1, b=2, c='str')

# the order must be arg, *args, **kwargs
def func3(a, *args, **kwargs):
    print(a, args, kwargs)

func3(1, 2, 3, 'a', 'b', 'c', d=1, e=2, f=3)
