'''
Created on 2013-6-1

@author: lj8175
'''
from EulerLib import isPrime
import itertools

if __name__ == '__main__':
    i,e = 1,8
    while True:
        i += 1
        if isPrime(i):
            for j in range(1,len(str(i))):
                for k in list(itertools.combinations(range(len(str(i))),j)):
                    s = 1 if 0 in k else 0
                    li,lr = list(str(i)),[]
                    for l in range(s,10):
                        for m in k:
                            li[m] = str(l)
                        if isPrime(int(''.join(li))): lr.append(int(''.join(li)))
                    if len(lr) >= e and i in lr: 
                        print i#,k,lr
                        exit(0)
            #print i
    pass