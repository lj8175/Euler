'''
Created on 2013-5-23

@author: joelliu
'''

def isPalindromic(x):
    s = str(x)
    for i in range(len(s)/2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

if __name__ == '__main__':
    num,x1,x2 = 0,0,0
    for i in range(999,0,-1):
        for j in range (999,0,-1):
            if isPalindromic(i*j):
                if i*j > num:
                    num, x1, x2 = i*j, i, j
                break
    print num,x1,x2