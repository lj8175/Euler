'''
Created on 2013-5-31

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

def isOdd(x):
    return x%2 == 0

if __name__ == '__main__':
    i = 1
    while True:
        i+=1
        if not isOdd(i) and not isPrime(i):
            flag = False
            for j in range(i):
                if isOdd(i-j) and isPrime(j):
                    k = int(math.sqrt((i-j)/2))
                    if ((i-j)/2) == k**2 : 
                        flag = True
            if not flag:
                    print i
                    break
            #else :
            #    print str(i)+'--'