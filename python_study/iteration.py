#!/usr/bin/python3

aList = list(range(10))
anIter = iter(aList)

while True:
    try:
        print(anIter.__next__())
    except StopIteration:
        break

print('Iteration completed.')
