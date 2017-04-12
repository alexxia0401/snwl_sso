#!/usr/bin/python3

'makeTextFile.py -- create text file'

import os


# get filename
while True:
    fname = input('Enter file name: ')
    if os.path.exists(fname):
        print("ERROR: '%s' already exists" % fname)
    else:
        break

# get file content (text) lines
all = []
print("\nEnter lines ('.' by itself to quit).\n")

# loop until user terminates input
while True:
    entry = input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.write('\n'.join(all))
fobj.close()
print('DONE!')
