#!/usr/bin/python3

def hello(name):
    return 'hello ' + name

#print(hello('John'))

def ptag(func):
    def modi(*args, **kwargs):
        result = '<p>' + func(*args, **kwargs) + '</p>'
        return result
    return modi

def divtag(func):
    def modi(*args, **kwargs):
        result = '<div>' + func(*args, **kwargs) + '</div>'
        return result
    return modi

@divtag
@ptag
def hello(name):
    return 'hello ' + name



print(hello('John'))
