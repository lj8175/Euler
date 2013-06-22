'''
Created on 2013-5-31

@author: lj8175
'''
import math
def isPrime(x):
    if x<=1 :return False
    elif x%2 == 0: return False
    elif x%3 == 0: return False
    elif x%5 == 0: return False
    elif x%7 == 0: return False
    for i in range(11,int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

if __name__ == '__main__':
    l = []
    for i in range(1000,10000):
        if isPrime(i): l.append(i)
    for i in range(len(l)):
        t1,t2 = l[i]+3330,l[i]+2*3330
        if t1 in l and t2 in l and len(set(str(t1))) == len(set(str(t1)+str(t2))):
            print l[i],t1,t2
        
    pass