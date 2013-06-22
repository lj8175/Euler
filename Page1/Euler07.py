'''
Created on 2013-5-23

@author: lj8175
'''
import math

def isPrime(x):
    if x <= 1:
        return False
    for i in range(2,int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

if __name__ == '__main__':
    num, i = 0, 2
    while num < 10001 :
        if isPrime(i):
            num += 1
        i += 1
    print i - 1
    pass