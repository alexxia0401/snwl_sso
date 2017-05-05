#!/usr/bin/python3

from time import ctime, sleep
import threading

'''test multi thread'''

def music(name):
    for i in range(2):
        print('I was listening to the music %s. %s' % (name, ctime()))
        sleep(1)

def movie(name):
    for i in range(2):
        print('I was watching the movie %s. %s' % (name, ctime()))
        sleep(5)

threads = []
    
t1 = threading.Thread(target=music, args=('As long as you love me',))
threads.append(t1)
t2 = threading.Thread(target=movie, args=('Titanic',))
threads.append(t2)

if __name__ == '__main__':

    for t in threads:
        t.setDaemon(True)
        t.start()
    
    t.join()
    print('all time %s' % ctime())
