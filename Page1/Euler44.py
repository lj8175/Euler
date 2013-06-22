'''
Created on 2013-5-31

@author: joelliu
'''

import math

def pentagonal(x):
    return x*(3*x-1)/2

def isPentagonal(x):
    if x <= 0 : return False
    y = x*2; y /= 3
    i = int(math.sqrt(y))
    while pentagonal(i) < x: i+=1
    return True if pentagonal(i) == x else False

if __name__ == '__main__':
    i,flag = 2,True
    while flag:
        for j in range(1,i):
            s = pentagonal(i) + pentagonal(j)
            d = pentagonal(i) - pentagonal(j)
            if isPentagonal(s) and isPentagonal(d):
                print d
                flag = False
        i+=1
    pass