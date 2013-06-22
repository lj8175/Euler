'''
Created on 2013-5-30

@author: lj8175
'''

def irrationalDecimal(x):
    i,s = 0,''
    while len(s) <= x:
        s += str(i)
        i += 1
    return s

if __name__ == '__main__':
    s = irrationalDecimal(1000000)
    print int(s[1])*int(s[10])*int(s[100])*int(s[1000])*int(s[10000])*int(s[100000])*int(s[1000000])
    pass