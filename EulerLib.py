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

if __name__ == '__main__':
    print set([3,3,2,4])
    pass