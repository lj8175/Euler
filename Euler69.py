'''
Created on 2013-12-9

@author: joelliu
'''
from EulerLib import dictPrime

'''
method1
http://en.wikipedia.org/wiki/Totient_function
http://www.mathblog.dk/project-euler-69-find-the-value-of-n-%E2%89%A4-1000000-for-which-n%CF%86n-is-a-maximum/
method2
http://www.itnosh.com/2010/07/Project_Euler_69.html
'''

def totient(num):
    ret,d = 1,dictPrime(num)
    for i in d:
        ret *= i**(d[i]-1)*(i-1)
    return ret

if __name__ == '__main__':
    '''
        #method1
        result,i = 1,1;
        while(result<1000000):
            if isPrime(i) :
                result = result*i
            i+=1
        result = result/(i-1)
        print result
    '''
    #
    maxT, x = 0, 0
    for i in range(2,1000001):
        if i*1.0/totient(i)>=maxT:
            maxT = i*1.0/totient(i)
            x = i
    print x#,maxT
    pass