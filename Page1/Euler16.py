'''
Created on 2013-5-25

@author: lj8175
'''

if __name__ == '__main__':
    s,num = str(2**1000),0
    for i in range(len(s)):
        num += int(s[i])
    print num
    pass