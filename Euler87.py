'''
Created on 2013-12-17

@author: joelliu
'''
import math
from EulerLib import isPrime

if __name__ == '__main__':
    known,primeList,resultSet = 50*1000000,[],set()
    for i in range(int(math.sqrt(known))+1+1):
        if isPrime(i):
            primeList.append(i)
    #print len(primeList)
    for i in primeList:
        for j in primeList:
            for k in primeList:
                num = i**2+j**3+k**4
                if num <= known:
                    #print i, j, k
                    resultSet.add(num)
                else: break
    print len(resultSet)
    pass