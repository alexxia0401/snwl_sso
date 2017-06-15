#!/usr/bin/python3

def occur(value, lis):
    count = 0
    for i in lis:
        if i == value:
            count += 1
    return count

print(occur(18, [1, 18, -7, 18, 5]))
