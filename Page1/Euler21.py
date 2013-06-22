'''
Created on 2013-5-26

@author: lj8175
'''

def listDivisors(x):
    ret = []
    for i in range(1,x):
        if x%i == 0:
            ret.append(i)
    return ret

def isAmicable(x):
    num = sum(listDivisors(x))
    if x!=num and x == sum(listDivisors(num)):
        return True
    return False
    

if __name__ == '__main__':
    nums = []
    for i in range(10000):
        if isAmicable(i):
            nums.append(i)
    print sum(nums)
