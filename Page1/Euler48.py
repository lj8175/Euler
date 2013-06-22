'''
Created on 2013-5-31

@author: lj8175
'''

if __name__ == '__main__':
    num = 0
    for i in range(1,1000+1):
        num += i**i
    print str(num)[-10:]