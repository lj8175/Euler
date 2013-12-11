'''
Created on 2013-12-11

@author: joelliu
'''
from EulerLib import gcd

if __name__ == '__main__':
    a,b = 3,7
    x,y,bestx,besty = 0,0,2,5
    for y in range(2,10**6+1):
        x = (a*y-1)/b
        if bestx*y < besty*x:
            bestx = x
            besty = y
    g = gcd(bestx,besty)
#     print "%s/%s"%(bestx/g,besty/g)
    print bestx/g
    pass