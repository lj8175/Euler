'''
Created on 2013-12-12

@author: joelliu
'''

from EulerLib import isPrime

def numPrimeWays(n, l):
    tl = [1]+[0]*n
    for i in l:
        for j in range(i,n+1):
            tl[j]+=tl[j-i]
    return tl

if __name__ == '__main__':
    known = 5000
    l = []
    for i in range(known):
        if isPrime(i):
            l.append(i)

    li = numPrimeWays(known,l)
    for i in range(known):
        if li[i]>known:
            print i#,li[i]
            break
    pass
