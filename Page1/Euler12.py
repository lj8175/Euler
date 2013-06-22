'''
Created on 2013-5-24

@author: lj8175
'''
import math

def triangle(x):
    return (1+x)*x/2

def listDivisors(x):
    ret = []
    for i in range(1,x+1):
        if x%i == 0:
            ret.append(i)
    return ret

def numDivisors(x):
    num,i,x2 = 0,1,int(math.sqrt(x));
    if x2**2 == x:
        num = 1
    while i<=x2 :
        if x%i == 0:
            num += 2
        i += 1
    if x2**2 == x:
        num -= 1
    return num

if __name__ == '__main__':
    i = 1
    while numDivisors(triangle(i)) <= 500:
        i += 1
    print triangle(i)
