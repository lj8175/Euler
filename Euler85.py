# -*- coding:utf-8 -*-
'''
Created on 2013年12月16日

@author: lj8175
'''
import sys

def keyXy(x,y):
    return str(x)+'-'+str(y)

d = {} #memo
def numRectangles(x,y):
    key = keyXy(x,y)
    if keyXy(x-1,y) in d:
        d[key] = d[keyXy(x-1,y)]+x*(y+1)*y/2
        return d[key]
    
    result = 0
    for i in range(1,x+1):
        for j in range(1,y+1):
            result+=(x+1-i)*(y+1-j)
    d[key] = result
    return d[key]
    pass

if __name__ == '__main__':
    saveArea, saveMin = 0, sys.maxint
    for x in range(1,2000+1):
        for y in range(1,2000+1):
            num = numRectangles(x, y)
            if abs(num-2000000)<saveMin:
                saveMin = abs(num-2000000)
                saveArea = x*y
            if num-2000000 > 0 : break
#         print x,y, saveMin,saveArea
    print saveArea#,len(d)
    pass