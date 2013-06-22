'''
Created on 2013-5-27

@author: lj8175
'''

def listDiagonal(x):
    l = [1]
    for i in range(1,x/2+1):
        for j in range(4):
            l.append(l[-1]+i*2) 
    return l

if __name__ == '__main__':
    print sum(listDiagonal(1001))
    pass