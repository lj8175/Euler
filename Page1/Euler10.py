'''
Created on 2013-5-23

@author: lj8175
'''
import math
import time

def isPrime(x):
    if x<=1 :return False
    elif x%2 == 0: return False if x!=2 else True
    elif x%3 == 0: return False if x!=3 else True
    elif x%5 == 0: return False if x!=5 else True
    elif x%7 == 0: return False if x!=7 else True
    for i in range(11,int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

if __name__ == '__main__':
    begin = time.clock()
    s = 0
    for i in range(int(2e6)):
        if isPrime(i):
            s += i
            #print i
    print s
    print time.clock() - begin
    pass