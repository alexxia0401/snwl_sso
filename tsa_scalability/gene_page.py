#!/usr/bin/env python

#<html>
#<head>
#<title>page1</title>
#</head>
#<body>
#This is page1.
#</body>
#</html>

def gene_page():
    for i in range(1,10001):
        PATH = '/var/www/html/page'
        FILE = PATH + str(i) + '.htm'
        fp = open(FILE, 'w')
        fp.write('<html>\n')
        fp.write('<head>\n')
        line = '<title>page' + str(i) + '</title>\n'
        fp.write(line)
        fp.write('</head>\n')
        fp.write('<body>\n')
        line = 'This is page' + str(i) + '.\n'
        fp.write(line)
        fp.write('</body>\n')
        fp.write('</html>\n')
        fp.close()

if __name__ == '__main__':
    gene_page()
