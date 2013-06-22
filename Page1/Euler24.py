'''
Created on 2013-5-26

@author: lj8175
'''
import itertools
#def permutation 

if __name__ == '__main__':
    p = itertools.permutations(range(10))
    ret = ''
    for i in list(p)[1000000-1]:
        ret += str(i)
    print ret