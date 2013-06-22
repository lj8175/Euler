'''
Created on 2013-5-31

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

if __name__ == '__main__':
    l,r,cont = [],1000000,0
    for i in range(r):
        if isPrime(i) : 
            l.append(i)
    #print len(l)#,l
    ml,m = [],0
    for i in range(len(l)):
        for j in range(cont,i+1):
            if i+1-j<len(ml): break
            tmp = sum(l[j:i+1])
            if tmp>=r : cont = j;continue
            if i!=j and isPrime(tmp):
                if len(l[j:i+1]) > len(ml):
                    ml,m = l[j:i+1],tmp
    print m
                