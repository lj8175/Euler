'''
Created on 2013-7-8

@author: lj8175

http://blog.dreamshire.com/2011/01/22/project-euler-problem-66-solution/
http://en.wikipedia.org/wiki/Chakravala_method
http://zh.wikipedia.org/wiki/%E6%B8%90%E8%BF%9B%E8%BF%9E%E5%88%86%E6%95%B0%E8%A1%A8%E7%A4%BA#.E5.AE.9A.E7.90.86_1
http://zh.wikipedia.org/wiki/%E4%BD%A9%E5%B0%94%E6%96%B9%E7%A8%8B#.E4.BD.A9.E5.B0.94.E6.96.B9.E7.A8.8B.E7.9A.84.E8.A7.A3
http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html
'''
from math import sqrt

def isSquare(x):
    return int(sqrt(x))**2 == x

def pell(d):
    p, k, x1, y, sd = 1, 1, 1, 0, sqrt(d)
 
    while k != 1 or y == 0:
        p = k * (p/k+1) - p
        p = p - int((p - sd)/k) * k
     
        x = (p*x1 + d*y) / abs(k)
        y = (p*y + x1) / abs(k)
        k = (p*p - d) / k
 
        x1 = x
 
    return x

if __name__ == '__main__':
    ret,largest = 0,0
    for x in range(2,1000):
        if isSquare(x) : continue
        if pell(x) > largest:
            largest = pell(x)
            ret = x
    print ret