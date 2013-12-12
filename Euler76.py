'''
Created on 2013-12-12

@author: joelliu
'''

#method1 : brute force.. too long time
def numWays1(n):
    result,l,pos = 0,[n],0
    while l[0] != 1:
        pos = (l.index(1) if 1 in l else len(l)) -1
        l[pos] -= 1 ; l = l[:pos+1]
        left = n - sum(l)
        while left>l[pos]:
            l.append(l[pos])
            left -= l[pos]
        l.append(left)
        result += 1
        print left,l
    return result

#method2: 0 1 2 4 6 10 14 21 29 41..
#http://oeis.org/A000065

#method3: http://www.mathblog.dk/project-euler-76-one-hundred-sum-integers/
def numWays3(n):
    l = [1]+[0]*n
    for i in range(1,n):
        for j in range(i,n+1):
            l[j]+=l[j-i]
    return l[n]

if __name__ == '__main__':
    known = 100
    print numWays3(100)
    pass