# -*- coding:utf-8 -*-
'''
Created on 2013年12月13日

@author: root
'''
def listWays(n):
    l = [1]+[0]*n
    for i in range(1,n+1):
        for j in range(i,n+1):
            l[j]+=l[j-i]
    return l

if __name__ == '__main__':
    known = 60000
    li = listWays(known)
    print li[-1]
    for i in range(known):
        if li[i] % 1000000 == 0:
            print i,li[i]
            break
    pass