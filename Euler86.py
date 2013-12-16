'''
Created on 2013-12-16

@author: joelliu
'''
#http://www.mathblog.dk/project-euler-86-shortest-path-cuboid/

from EulerLib import isSquare


if __name__ == '__main__':
    l,count,target = 2,0,1000000
    while count < target:
        l+=1
        for wh in range(3,2*l+1):
            if isSquare(wh**2+l**2):
                count += wh/2 if wh<=l else 1+l-(wh+1)/2
    print l
    pass