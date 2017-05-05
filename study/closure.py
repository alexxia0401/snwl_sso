#!/usr/bin/python3

def knights(dis):
    def inner():
        return 'The words are: %s' % dis
    return inner

a = knights('hello')
b = knights('world')

print(a())
print(b)
