#!/usr/bin/python3

from time import ctime, sleep

'''test multi thread'''

def music(name):
    for i in range(2):
        print('I was listening to the music %s. %s' % (name, ctime()))
        sleep(1)

def movie(name):
    for i in range(2):
        print('I was watching the movie %s. %s' % (name, ctime()))
        sleep(5)

if __name__ == '__main__':
    music('As long as you love me')
    movie('Titanic')
    print('all time %s' % ctime())
