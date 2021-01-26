#!/usr/bin/python3

def hello(name):
    return 'hello ' + name

#print(hello('John'))

def tagname(tag):
    def ptag(func):
        def modi(*args, **kwargs):
            result = '<' + tag + '>'+ func(*args, **kwargs) + '</' + tag + '>'
            return result
        return modi
    return ptag

@tagname('p')
def hello(name):
    return 'hello ' + name



print(hello('John'))
