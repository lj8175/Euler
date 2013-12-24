'''
Created on 2013-12-23

@author: joelliu
'''

s = set()
def end89(i):
    global s
    if i in s : return True
    n,stmp = i,set()
    while (n!=1 and n!=89):
        ntmp = 0
        for c in str(n):
            ntmp += int(c)*int(c)
        n = ntmp
        if n in s :
            s = s.union(stmp)
            return True
        stmp.add(n)
    if n == 89:
        s = s.union(stmp)
        return True
    if n == 1:
        return False

if __name__ == '__main__':
    result = 0
    for i in range(1,10000000):
        if end89(i):
            result+=1
#         if i%10000 == 0:
#             print i,len(s);
    print result#, len(s)
    pass