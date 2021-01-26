#!/usr/bin/python3

def square(num):
    return num * num

print(square(5))

a = lambda num: num * num  # notice there is no return
print(a(6))
