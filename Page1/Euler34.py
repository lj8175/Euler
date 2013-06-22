'''
Created on 2013-5-29

@author: joelliu
'''

def factorial(x):
    if x == 0 : return 1
    return reduce(lambda x,y:x*y, range(1,x+1)) 

def listNum():
    l = []
    for i in range(3,factorial(9)*7+1):
        tmp = 0
        for j in str(i):
            tmp += factorial(int(j))
        if tmp == i:
            l.append(i)
        #print i, l
    return l

if __name__ == '__main__':
    print sum(listNum())
    pass