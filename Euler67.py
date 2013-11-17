'''
Created on 2013-11-17

@author: lj8175
'''

import re

def readTriagle():
    fHandler = open("Euler67.txt")
    d = []
    for line in fHandler:
        strlist = re.split(" |\n", line.strip())
        dtmp = []
        for num in strlist:
            dtmp.append(int(num))
        d.append(dtmp)
    return d
    
def maxTriaglePath(d):
    for i in range(len(d)-2,-1,-1):
        for j in range(0,i+1):
            d[i][j] = d[i][j] + max(d[i+1][j], d[i+1][j+1])
    return d[0][0]


if __name__ == '__main__':
    d = readTriagle()
    print maxTriaglePath(d)