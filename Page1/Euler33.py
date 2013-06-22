'''
Created on 2013-5-29

@author: joelliu
'''

def nonTrivial():
    d = {}
    for i in range(11,99):
        for j in range(i,99+1):
            s = set(str(i)).intersection(set(str(j)))
            if len(s) == 1 and list(s)[0]!='0' and len(set(str(i))) == 2 and len(set(str(i)))==len(set(str(j))):
                si = int(str(i).strip(''.join(s)))
                sj = int(str(j).strip(''.join(s)))
                if sj != 0 and si < sj and si/float(sj) == i/float(j):
                    d[i] = j
    return d

def gcd(m, n):
    while n:
        m, n = n, m % n
    return m

if __name__ == '__main__':
    d = nonTrivial()
    numerator,denominator = 1,1
    for i in d:
        numerator *= i
        denominator *= d[i]
    print denominator/gcd(numerator,denominator)