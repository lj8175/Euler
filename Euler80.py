'''
Created on 2013-12-13

@author: joelliu
'''
from EulerLib import isSquare

#http://www.mathblog.dk/project-euler-80-digits-irrational-square-roots/
#http://www.afjarvis.staff.shef.ac.uk/maths/jarvisspec02.pdf

def nsqrt(m, n):
    limit = 10**(n+1)
    a,b = 5*m, 5
    while (b<limit):
        if a>b:
            a-=b; b+=10;
        else:
            a*=100; b=(b/10)*100+5
    return b/100

if __name__ == '__main__':
    result = 0
    for i in range(100+1):
        if not isSquare(i):
            result+=sum(int(t) for t in str(nsqrt(i, 100)))
    print result