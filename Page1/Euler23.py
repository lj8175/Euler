'''
Created on 2013-5-26

@author: lj8175
'''

import math

def listDivisors(x):
    ret = []
    if x > 1: ret.append(1)
    for i in range(2,int(math.sqrt(x))+1):
        if x%i == 0:
            ret.append(i)
            if i != x/i : ret.append(x/i)
    return ret

def isAbundant(x):
    if sum(listDivisors(x)) > x:
        return True
    return False

def isSumOfTwoAbundant(x):
    for i in range(x/2+1):
        if isAbundant(i) and isAbundant(x-i):
            return True
    return False

if __name__ == '__main__':
    ret = []
    for i in range(28123+1):
        if not isSumOfTwoAbundant(i): 
            ret.append(i)
    print sum(ret)