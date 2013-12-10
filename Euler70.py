'''
Created on 2013-12-10

@author: joelliu
'''
from Euler69 import totient
import math
from EulerLib import isPrime

'''
method1 : several hours
http://www.itnosh.com/2010/07/Project_Euler_70.html

method2

'''


if __name__ == '__main__':
    #method2
    s = int(math.sqrt(10**7))
    pl,maxRatio, best = [], 1000, 0
    for i in range(s-1000, s+2000):
        if isPrime(i):
            pl.append(i)
    for i in range(len(pl)):
        for j in range(i, len(pl)):
            num = pl[i]*pl[j]
            if num > 10**7 : break
            phi = (pl[i]-1)*(pl[j]-1)
            ratio = num*1.0/phi
            if sorted(str(num)) == sorted(str(phi)) and ratio<maxRatio:
                maxRatio = ratio
                best = num
    print best#, maxRatio
    '''
    #method1
    minT, x = 1000, 0
    for i in range(2,10**7):
        if sorted(str(i)) == sorted(str(totient(i))):
            print i,totient(i)
            if i*1.0/totient(i)<minT:
                minT = i*1.0/totient(i)
                x = i
    print x#, minT
    pass
    '''
    