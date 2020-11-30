#!/usr/bin/python3
'''
An example of reading and writing Unicode strings:
Writes a Unicode string to a file in utf-8 and reads it back in.
'''
CODEC = 'utf-8'
FILE = 'unicode.txt'

hello_out = 'Hello World\n'  # In py3, str is already unicode
# bytes_out = hello_out.encode(CODEC)
f = open(FILE, 'w', encoding=CODEC)  # In py3, no need to use encode() & decode(), just use encoding= when open file
f.write(hello_out)
f.close()

f = open(FILE, 'r', encoding=CODEC)
hello_in = f.read()
f.close()
# hello_in = bytes_in.decode(CODEC)
print(hello_in, end='')
