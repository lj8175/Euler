'''
Created on 2013-7-6

@author: lj8175
'''

import math

if __name__ == '__main__':
    ret = 0
    for x in range(2,10000+1):
        r = limit = int(math.sqrt(x))
        if limit**2 == x: continue
        k, period = 1, 0
        while k!=1 or period==0:
            k = (x-r*r)/k
            r = ((limit+r)/k)*k-r
            period += 1
        if period % 2 == 1:
            ret += 1
    print ret
        