'''
Created on 2013-5-29

@author: lj8175
'''

def isPalindromic(s):
    for i in range(len(s)/2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

def sumPalindromes(x):
    num = 0
    for i in range(x):
        if isPalindromic(str(i)) and isPalindromic(str(bin(i))[2:]):
            num += i
            #print i
    return num

if __name__ == '__main__':
    print sumPalindromes(1000000) 
    pass