'''
Created on 2013-12-11

@author: joelliu
'''

#http://en.wikipedia.org/wiki/Farey_sequence

from EulerLib import gcd
import time
import math

if __name__ == '__main__':
    ts = time.time()
    a, b, c, d, x, y = 1, 3, 1, 2, 0, 0
    result = 0
    for y in range(5,12000+1):
        minx = int(math.ceil(float(a*y+1)/b))
        maxx = (c*y-1)/d
        for x in range(minx, maxx+1):
            if gcd(y,x) == 1:
                result += 1
        #print y,minx,maxx
    print result#,time.time()-ts
