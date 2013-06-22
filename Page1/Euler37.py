'''
Created on 2013-5-29

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

def elevenTruncatablePrimes():
    l,i = [],11
    while len(l) < 11:
        if isPrime(i):
            flag = True
            for j in range(1,len(str(i))):
                if isPrime(int(str(i)[j:])) == False or isPrime(int(str(i)[:j])) == False:
                    flag = False
                    break
            if flag : l.append(i)
        #print i
        i += 1
    return l

if __name__ == '__main__':

    l = elevenTruncatablePrimes()
    print sum(l) #, l
    pass