#!/ usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2013-5-22

@author: joelliu
'''

if __name__ == '__main__':
    num = 0
    for i in range(1000):
        if i%3==0 or i%5==0:
            num+=i 
    print num