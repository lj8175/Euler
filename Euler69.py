'''
Created on 2013-12-9

@author: joelliu
'''
from EulerLib import isPrime

#http://en.wikipedia.org/wiki/Totient_function
#http://www.mathblog.dk/project-euler-69-find-the-value-of-n-%E2%89%A4-1000000-for-which-n%CF%86n-is-a-maximum/


if __name__ == '__main__':
    result,i = 1,1;
    while(result<1000000):
        if isPrime(i) :
            result = result*i
        i+=1
    result = result/(i-1)
    print result