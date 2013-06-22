'''
Created on 2013-5-23

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

def listPrime(num):
    i,ret = 2,{}
    while num > 1:
        if isPrime(i):
            while num % i == 0:
                num /= i
                if ret.has_key(i):
                    ret[i] +=1
                else:
                    ret[i] = 1
        i += 1
    return ret

if __name__ == '__main__':
    tem,ret = [],{}
    for i in range(21):
        tem.append(listPrime(i))

    for i in range(len(tem)):
        for j in tem[i]:
            if ret.has_key(j):
                if ret[j] < tem[i][j]:
                    ret[j] = tem[i][j]
            else:
                ret[j] = tem[i][j]
    print ret
    num = 1
    for i in ret:
        num *= i**ret[i]
    print num