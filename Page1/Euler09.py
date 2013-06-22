'''
Created on 2013-5-23

@author: lj8175
'''

if __name__ == '__main__':
    for i in range(1,1000):
        for j in range(1,1000):
            k = 1000-i-j
            if k <= 0:
                break
            if k**2 == (i**2+j**2):
                print i,j,k, i*j*k
    pass