'''
Created on 2013-6-5

@author: joelliu
'''
from EulerLib import isPrime

def listDiagonal(x):
    l = [1]
    for i in range(1,x/2+1):
        for j in range(4):
            l.append(l[-1]+i*2) 
    return l

if __name__ == '__main__':
    i,np = 1,0
    while True:
        i += 2
        l = listDiagonal(i)
        for j in l[-4:] : 
            if isPrime(j):np+=1
        if np*1.0/len(l) < 0.1:
            print i
            break
        #print i, np*1.0/len(l)
    pass