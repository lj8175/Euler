'''
Created on 2013-12-11

@author: joelliu
'''
from Euler69 import totient

'''
method2:
http://www.mathblog.dk/project-euler-72-reduced-proper-fractions/
'''

if __name__ == '__main__':
    #method2
    total = 0
    l = list(range(10**6+1))
    for i in range(2,len(l)):
        if l[i] == i:
            j=i
            while j+i<len(l):
                j+=i;
                l[j] = l[j]*(i-1)/i
            l[i] -= 1
        total += l[i]
    print total
    pass
    '''
    #method2: several minitus
    num = 0
    for i in range(2,10**6+1):
        num+=totient(i)
    print num
    pass
    '''