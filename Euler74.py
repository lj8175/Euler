'''
Created on 2013-12-11

@author: joelliu
'''
import time
from EulerLib import factorial

d = {} #memo

def nonrepeatchain(n):
    nl = [n]
    while True:
        t = 0
        ns = str(n)
        for c in ns:
            t+=factorial(int(c))
        n = t
        if n in d: return nl+d[n] #memo
        if t in nl:
            break
        else:
            nl.append(t)
    return nl

if __name__ == '__main__':
    ts = time.time()
    result = 0
    for i in range(10**6):
        d[i] = nonrepeatchain(i) #memo
        if len(d[i]) == 60:
            result+=1
            #print i,nonrepeatchain(i) 
    print result#, time.time()-ts
    pass