'''
Created on 2013-5-25

@author: lj8175
'''

def listCollatz(x):
    ls = []
    ls.append(x)
    while x!=1:
        if x%2 == 0:
            x /=2
        else:
            x = 3*x+1
        ls.append(x)
    return ls
    
if __name__ == '__main__':
    largest, ret = 0, 0
    for i in range(1,1000000):
        l = len(listCollatz(i))
        if l > largest:
            largest, ret = l, i 
    print ret
