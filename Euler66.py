'''
Created on 2013-7-8

@author: lj8175
'''
import math

def isSquare(x):
    return int(math.sqrt(x))**2 == x

def quadraticDiophantine(d):
    if isSquare(d): return [0, 0]
    y, flag= 0, True
    while flag:
        y += 1
        if isSquare(d*y**2+1): flag = False
        print y
    return [int(math.sqrt(d*y**2+1)), y]

if __name__ == '__main__':
    print quadraticDiophantine(999)
    exit(0)
    largest = 0
    for i in range(2,1000+1):
        l = quadraticDiophantine(i)
        if l[0] >= largest : largest = l[0]
        print i
    print largest                
    pass