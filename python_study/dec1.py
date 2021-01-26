#!/usr/bin/python3

def hello(name):
    return 'hello ' + name

#print(hello('John'))

def ptag(func):
    def modi(*args, **kwargs):
        result = '<p>' + func(*args, **kwargs) + '</p>'
        return result
    return modi

@ptag
def hello(name):
    return 'hello ' + name

print(hello('John'))
