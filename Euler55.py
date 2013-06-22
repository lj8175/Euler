'''
Created on 2013-6-4

@author: lj8175
'''

def isPalindromic(s):
    for i in range(len(s)/2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

def isLychrel(x):
    i = 0
    while i < 50:
        x += int(str(x)[::-1])
        if isPalindromic(str(x)):
            return False
        i += 1
    return True

if __name__ == '__main__':
    l = []
    for i in range(10000):
        if isLychrel(i): 
            l.append(i)
    print len(l)#,l
    pass