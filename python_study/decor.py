#!/usr/bin/python3

def sum(a, b):
    return a + b

print(sum(3, 5))



def dec(fun):
    def modi(*args, **kwargs):
        print('I did my own things here.')
        #print(fun.__name__)
        result = fun(*args, **kwargs)
        return result
    return modi


print('decoration function...')
a = dec(sum)
print(a(3, 5))
print('stopped...')

@dec
def sum(a, b):
    return a + b
print(sum(3, 5))
