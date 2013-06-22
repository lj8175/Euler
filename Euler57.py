'''
Created on 2013-6-5

@author: joelliu
'''


def sqrt2(x,d={}):
    if x <= 0: return 0
    if x == 1: return 2
    if x == 2: return 5
    if x-2 not in d:
        d[x-2] = sqrt2(x-2,d)
    if x-1 not in d:
        d[x-1] = sqrt2(x-1,d)
    return 2*d[x-1] + d[x-2]

if __name__ == '__main__':
    num = 0
    for i in range(1000):
        if len(str(sqrt2(i-1)+sqrt2(i))) > len(str(sqrt2(i))):
            num += 1
        #print i
    print num
    pass