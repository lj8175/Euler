'''
Created on 2013-5-22

@author: joelliu
'''

def fib(x):
    if x==1:
        return 1
    elif x==2:
        return 2
    else:
        return fib(x-1)+fib(x-2)

if __name__ == '__main__':
    i,num,s=1,1,0
    while num <= 4e6 :
        s += 0 if (num%2) else num
        i,num = i+1, fib(i)
    print s