'''
Created on 2013-5-30

@author: lj8175
'''

import itertools

if __name__ == '__main__':
    l = []
    for i in list(itertools.permutations(range(9,-1,-1))):
        s = ''.join([str(j) for j in i])
        if s[0] == 0 : break
        if int(s[1:4])%2==0 and int(s[2:5])%3==0 and int(s[3:6])%5==0 and int(s[4:7])%7==0 and int(s[5:8])%11==0 and int(s[6:9])%13==0 and int(s[7:10])%17==0:
            l.append(int(s))
            print s
    print sum(l)# , l
