'''
Created on 2013-5-27

@author: lj8175
'''

def numDistinct(low, high):
    l = []
    for i in range(low, high+1):
        for j in range(low, high+1):
            l.append(i**j)
    return len(set(l))

if __name__ == '__main__':
    print numDistinct(2, 100)
    pass