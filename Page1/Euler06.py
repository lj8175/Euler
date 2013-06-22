'''
Created on 2013-5-23

@author: lj8175
'''

if __name__ == '__main__':
    num,sum1,sum2=100,0,0
    for i in range(num+1):
        sum1 += i**2
        sum2 += i 
    print sum2**2-sum1