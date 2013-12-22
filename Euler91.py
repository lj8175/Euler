# -*- coding:utf-8 -*-
'''
Created on 2013年12月22日

@author: lj8175
'''

def pointDistanceSquare(x1,y1,x2=0,y2=0):
    return (x1-x2)**2 + (y1-y2)**2

if __name__ == '__main__':
    known,result = 50,0
    for x1 in range(1,known+1):
        for y1 in range(known+1):
            for x2 in range(known+1):
                for y2 in range(y1,known+1):
                    l = []
                    l.append(pointDistanceSquare(x1, y1))
                    l.append(pointDistanceSquare(x2, y2))
                    l.append(pointDistanceSquare(x1, y1, x2, y2))
                    l = sorted(l)
                    if(0 not in l and l[0] + l[1] == l[2]):
                        result += 1
                        #print x1, y1, x2, y2
        #print x1
    print result
    pass