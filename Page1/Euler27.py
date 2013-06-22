'''
Created on 2013-5-27

@author: joelliu
'''

import math

def isPrime(x):
    if x <= 1:
        return False
    for i in range(2,int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def numPrimes(a, b):
    if abs(a) >= 1000 or abs(b) >= 1000 : return "a and b should in |1000|"
    ret,n = 0,0
    while True:
        if isPrime(n**2+a*n+b):
            ret+=1
        else: break
        n += 1
    return ret

if __name__ == '__main__':
    a, b, gt = 0, 0, 0
    for i in range(1-1000, 1000):
        for j in range(1-1000, 1000):
            tmp = numPrimes(i, j)
            if tmp > gt:
                a,b,gt = i,j,tmp
    print a*b