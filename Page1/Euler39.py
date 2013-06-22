'''
Created on 2013-5-30

@author: joelliu
'''

def listSolutions(x):
    l = []
    for i in range(1,x):
        for j in range(1,x-i):
            if i**2+j**2==(x-i-j)**2:
                l.append(sorted([i,j,x-i-j]))
                break
    return l

if __name__ == '__main__':
    largest, num = 0, 0
    for x in range(3,1000+1):
        l,ret = listSolutions(x),[]
        [ret.append(i) for i in l if not i in ret]
        #print x, ret
        if len(ret) > largest:
            num = x
            largest = len(ret)
    print num
    pass