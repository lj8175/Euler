'''
Created on 2013-6-4

@author: lj8175
'''

if __name__ == '__main__':
    m = 0
    for i in range(100):
        for j in range(100):
            num,tmp = i**j,0
            for k in str(num):
                tmp += int(k)
            if tmp > m:
                m = tmp
    print m
    pass