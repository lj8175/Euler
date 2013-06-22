'''
Created on 2013-5-31

@author: joelliu
'''
import math

def triangle(x):
    return x*(x+1)/2

def isTriangle(x):
    if x <= 0 : return False
    i = int(math.sqrt(x*2))
    return True if triangle(i) == x else False

def pentagonal(x):
    return x*(3*x-1)/2

def isPentagonal(x):
    if x <= 0 : return False
    i = int(math.sqrt(x*2/3))
    while pentagonal(i) < x: i+=1
    return True if pentagonal(i) == x else False

def hexagonal(x):
    return x*(2*x-1)

def isHexagonal(x):
    if x<=0 : return False
    i = int(math.sqrt(x/2))
    while hexagonal(i) < x: i+=1
    return True if hexagonal(i) == x else False

if __name__ == '__main__':
    i = 286
    while True:
        x = triangle(i)
        if isPentagonal(x) and isHexagonal(x):
            print x
            break
        i+=1
    pass