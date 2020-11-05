#!/usr/bin/env python3

file_name = input("Pls. enter file name: ")
file_obj = open(file_name, 'r')
data = file_obj.readlines()  # data is a list
file_obj.close()

for read_line in data:
    print(read_line, end="")
