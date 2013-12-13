'''
Created on 2013-12-13

@author: joelliu
'''

import re
import sys

tl = [
[131,673,234,103,18],
[201,96,342,965,150],
[630,803,746,422,111],
[537,699,497,121,956],
[805,732,524,37,331]
]

def readSquare():
    fHandler = open("Euler81.txt")
    d = []
    for line in fHandler:
        strlist = re.split(",", line.strip())
        dtmp = []
        for num in strlist:
            dtmp.append(int(num))
        d.append(dtmp)
    return d


#method1: brute force
def minPath(l,x,y):
    #print x,y
    if x == 0:
        return sum(l[0][:y+1])
    if y == 0:
        ret = l[x][0]
        for i in range(x):
            ret += l[i][0]
        return ret
    return l[x][y]+min(minPath(l,x-1,y), minPath(l,x,y-1))
    pass

#method2: brute force add memo
def minPathMemo(l,x,y,d={}):
    #print x,y
    if x == 0:
        return sum(l[0][:y+1])
    if y == 0:
        ret = l[x][0]
        for i in range(x):
            ret += l[i][0]
        return ret
    key, keyUp, keyLeft= str(x)+'-'+str(y), str(x-1)+'-'+str(y), str(x)+'-'+str(y-1)
    if keyUp not in d:
        d[keyUp] = minPathMemo(l,x-1,y,d)
    if keyLeft not in d:
        d[keyLeft] = minPathMemo(l,x,y-1,d)
    d[key] = l[x][y]+min(d[keyUp],d[keyLeft])
    return d[key]
    pass

#method3: dynamic programming
def minPathDynamic(l):
    for n in range(len(l)+len(l[0])-1):
        for i in range(n+1):
            j = n-i
            if i<len(l) and j<len(l[0]):
                #print i,j
                up = l[i-1][j] if i-1>=0 else sys.maxint
                left = l[i][j-1] if j-1>=0 else sys.maxint
                l[i][j] += min(up,left) if min(up,left)!=sys.maxint else 0
    return l[len(l)-1][len(l[0])-1]
    pass



if __name__ == '__main__':
    '''
    #method1
    print minPath(tl, len(tl)-1,len(tl[0])-1) 
    '''
    
    '''
    #method2
    tl = readSquare()
    #d={}
    #print minPathMemo(tl, len(tl)-1,len(tl[0])-1,d)
    #print d
    print minPathMemo(tl, len(tl)-1,len(tl[0])-1)
    '''
    #method3
    tl = readSquare()
    print minPathDynamic(tl)
    
    pass