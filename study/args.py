#!/usr/bin/python3

def show(a, *args, **kwargs):
    print('arg1: %s' % a)
    for i in args:
        print('each arg is: %s' % i)

    for i in kwargs:
        print('each arg is: %s %s' % (i, kwargs[i]))

show('hello', 'world', 123, 'heihei', ip='192.168.10.3', port=80)


