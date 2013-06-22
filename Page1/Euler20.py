'''
Created on 2013-5-26

@author: lj8175
'''

def factorial(x):
    return reduce(lambda x,y:x*y, range(1,x+1)) 

if __name__ == '__main__':
    s = str(factorial(100))
    num = 0
    for i in s:
        num += int(i)
    print num