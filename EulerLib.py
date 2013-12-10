'''
Created on 2013-6-1

@author: lj8175
'''
import math
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

def factorial(x):
    if x == 0 : return 1
    return reduce(lambda x,y:x*y, range(1,x+1)) 

def gcd(x, y):
    if x<y : return gcd(y,x);
    if y==0 : return x;
    if x%2==0:
        if y%2==0:
            return gcd(x>>1, y>>1)<<1;
        else:
            return gcd(x>>1, y);
    else:
        if y%2==0:
            return gcd(x, y>>1);
        else:
            return gcd(y,x-y);
        
def dictPrime(num):
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
    print set([3,3,2,4])
    pass