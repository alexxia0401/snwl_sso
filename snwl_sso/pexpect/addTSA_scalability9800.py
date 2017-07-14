#!/usr/bin/python3

'''
For testing TSA scalability test on SM9800, this script adds MAX 512 TSA agents.
'''


import addTSA

def repeat(c, key, wanip, m = 63):
    for i in range(1, m):
        tsaAgentIp = '192.168.' + str(c) + '.' + str(i)
        addTSA.addTSA(wanip, tsaAgentIp, key)

if __name__ == '__main__':
    for j in range(81, 89):
        repeat(j, '123456', '10.0.0.67')

    repeat(89, '123456', '10.0.0.67', 17)
