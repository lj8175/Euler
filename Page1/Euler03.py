'''
Created on 2013-5-22

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


if __name__ == '__main__':
    i,num = 2,600851475143
    while num > 1:
        if isPrime(i):
            while num % i == 0:
                num = num / i
                print num,i
        i += 1