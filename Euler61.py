'''
Created on 2013-6-7

@author: lj8175
'''
import math

def triangle(x):
    return x*(x+1)/2

def square(x):
    return x**2

def pentagonal(x):
    return x*(3*x-1)/2

def hexagonal(x):
    return x*(2*x-1)

def heptagonal(x):
    return x*(5*x-3)/2

def octagonal(x):
    return x*(3*x-2)

def isTriangle(x):
    if x <= 0 : return False
    i = int(math.sqrt(x*2))
    return True if triangle(i) == x else False

def isSquare(x):
    if x <= 0 : return False
    i = int(math.sqrt(x))
    return True if square(i) == x else False

def isPentagonal(x):
    if x <= 0 : return False
    i = int(math.sqrt(x*2/3))
    while pentagonal(i) < x: i+=1
    return True if pentagonal(i) == x else False

def isHexagonal(x):
    if x<=0 : return False
    i = int(math.sqrt(x/2))
    while hexagonal(i) < x: i+=1
    return True if hexagonal(i) == x else False

def isHeptagonal(x):
    if x<=0 : return False
    i = int(math.sqrt(x*2/5))
    while heptagonal(i) < x: i+=1
    return True if heptagonal(i) == x else False

def isOctagonal(x):
    if x<=0 : return False
    i = int(math.sqrt(x/3))
    while octagonal(i) < x: i+=1
    return True if octagonal(i) == x else False

def isTSPHHO(x,l):
    if 3 not in l:
        if isTriangle(x):return 3
    if 4 not in l:
        if isSquare(x): return 4
    if 5 not in l:
        if isPentagonal(x): return 5
    if 6 not in l:
        if isHexagonal(x): return 6
    if 7 not in l:
        if isHeptagonal(x): return 7
    if 8 not in l:
        if isOctagonal(x): return 8
    return 0

if __name__ == '__main__':
    for i in range(1010,10000):
        ll = []
        if int(str(i)[2:4]) < 10 :continue
        ri = isTSPHHO(i, ll)
        if ri != 0: ll.append(ri)
        else : continue
        for j in range(10,100):
            ll = [ri]
            rj = isTSPHHO(int(str(i)[2:4]+str(j)), ll)
            if rj != 0: ll.append(rj)
            else : continue
            for k in range(10,100):
                ll = [ri,rj]
                rk = isTSPHHO(int(str(j)+str(k)), ll)
                if rk != 0: ll.append(rk);
                else : continue
                for l in range(10,100):
                    ll = [ri,rj,rk]
                    rl = isTSPHHO(int(str(k)+str(l)), ll)
                    if rl != 0: ll.append(rl);
                    else : continue
                    for m in range(10,100):
                        ll = [ri,rj,rk,rl]
                        rm = isTSPHHO(int(str(l)+str(m)), ll)
                        if rm != 0: ll.append(rm);
                        else : continue
                        for n in range(10,100):
                            ll = [ri,rj,rk,rl,rm]
                            rn = isTSPHHO(int(str(m)+str(n)), ll)
                            if rn != 0: 
                                ll.append(rn);
                                if str(n) == str(i)[:2]:
                                    #print i,j,k,l,m,n,ll
                                    print i+int(str(i)[2:]+str(j))+int(str(j)+str(k))+int(str(k)+str(l))+int(str(l)+str(m))+int(str(m)+str(n))
                                    exit(0)
                            else : continue
    pass









