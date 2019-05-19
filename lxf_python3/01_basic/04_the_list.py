#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
print('classmates.pop() =', classmates.pop())
print('classmates =', classmates)

classmates.append('Alex')
print("classmates.append('Alex')", classmates)
classmates.insert(1, 'Peter')
print("classmates.insert(1, 'Peter')", classmates)
classmates.pop(0)
print("classmates.pop(0)", classmates)
classmates[2] = 'Lawfer'
print(classmates)

print("\n正序显示")
for i in range(len(classmates)):
    print(classmates[i])

print("\n倒序显示")
for i in range(-1, -(len(classmates)+1), -1):
    print(classmates[i])

print("\nprint 'php' element")
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s[2][1])
