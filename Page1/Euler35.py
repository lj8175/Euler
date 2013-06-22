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

def numPrimes(x):
    num = 0
    for i in range(x):
        if isPrime(i) :
            flag = True
            for j in range(len(str(i))):
                if isPrime(int(str(i)[j+1:]+str(i)[0:j+1])) == False:
                    flag = False
            if flag : num+=1
        #print i
    return num

if __name__ == '__main__':
    print numPrimes(1000000)
    pass