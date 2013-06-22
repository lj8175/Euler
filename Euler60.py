'''
Created on 2013-6-6

@author: lj8175
'''
from EulerLib import isPrime

def isPrimePair(x,y):
    if isPrime(int(str(x)+str(y))) and isPrime(int(str(y)+str(x))):
        return True
    return False

def isPrimeToOthres(x,l):
    for i in l:
        if not isPrimePair(x, i):
            return False
    return True

if __name__ == '__main__':
#     li = [3,7]
#     print li.index(3)
#     print isPrimeToOthres(311, [23]);
#     exit(0)
    
    m,li = 10000,[]
    for i in range(m):
        if isPrime(i): 
            li.append(i)
    
    for i in li:
        for j in li[li.index(i)+1:]:
            ls = [i]
            if isPrimeToOthres(j, ls): ls.append(j)
            else: continue
            for k in li[li.index(j)+1:]:
                ls = [i,j]
                if isPrimeToOthres(k, ls): ls.append(k)
                else: continue
                for l in li[li.index(k)+1:]:
                    ls = [i,j,k]
                    if isPrimeToOthres(l, ls): ls.append(l); #print ls
                    else: continue
                    for m in li[li.index(l)+1:]:
                        if isPrimeToOthres(m, ls): 
                            ls.append(m)
                            print sum(ls)#,ls
                            exit(0)
    