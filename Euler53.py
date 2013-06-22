'''
Created on 2013-6-1

@author: lj8175
'''
from EulerLib import factorial

def numCombination(n,m):
    return factorial(n)/(factorial(m)*factorial(n-m))

if __name__ == '__main__':
    num = 0
    for i in range(1,100+1):
        for j in range(i+1):
            if numCombination(i, j)>1000000:
                num += 1
    print num
    pass