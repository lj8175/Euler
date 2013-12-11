'''
Created on 2013-12-11

@author: joelliu
'''
from EulerLib import gcd

'''
http://en.wikipedia.org/wiki/Pythagorean_triple
a = m*m-n*n 
b = 2*m*n
c = m*m+n*n
'''

import math

if __name__ == '__main__':
    known = 1500000
    resultd, result = {}, 0
    maxm = int(math.sqrt(known/2))
    for m in range(2,maxm):
        for n in range(1,m):
            if (m+n)%2==1 and gcd(m,n)==1:
                a = m*m-n*n 
                b = 2*m*n
                c = m*m+n*n
                l = a+b+c
                abc = sorted([a,b,c])
                i = 1
                while i*l <= known:
                    iabc = [i*x for x in abc]
                    if i*l in resultd : 
                        if iabc not in resultd[i*l] : resultd[i*l].append(iabc) 
                    else: resultd[i*l] = [iabc]
                    i += 1
    for i in resultd:
        if len(resultd[i]) == 1:
            result += 1
    print result
            
    pass