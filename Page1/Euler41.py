'''
Created on 2013-5-30

@author: lj8175
'''
import math
import itertools

def isPrime(x):
    if x <= 1:
        return False
    for i in range(2,int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


if __name__ == '__main__':
    for i in range(9,1,-1):
        for j in list(itertools.permutations(range(i,0,-1))):
            #print j
            if isPrime(int(''.join([str(k) for k in j]))):
                print int(''.join([str(k) for k in j]))
                exit(0)
    pass