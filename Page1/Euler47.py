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

def listPrime(num):
    i,ret = 2,{}
    if isPrime(num) : return {num:1}
    while num > 1:
        if isPrime(i):
            while num % i == 0:
                num /= i
                if ret.has_key(i):
                    ret[i] +=1
                else:
                    ret[i] = 1
            if isPrime(num):
                ret[num] = 1
                return ret
        i += 1
    return ret

if __name__ == '__main__':
    l,i,con = [0,1,1],3,4
    #print listPrime(79145)
    #exit(0)
    while True:
        i += 1
        l.append(len(listPrime(i)))
        flag = True
        for j in range(-con,0):
            if l[j] != con :flag = False
        if flag : 
            print i-con+1
            break
        #print i, l[-1], l[-2], l[-3], l[-4] 
    pass