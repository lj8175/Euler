'''
Created on 2013-12-18

@author: joelliu
'''

def num2roman(x):
    result = ''
    for i in range(x/1000):
        result += 'M'
    x = x%1000
    if x>=900:
        result += 'CM'
    elif x>=500:
        result += 'D'
        for i in range((x-500)/100):
            result += 'C'
    elif x>=400:
        result += 'CD'
    else :
        for i in range(x/100):
            result += 'C'
    x = x%100
    if x>=90:
        result += 'XC'
    elif x>=50:
        result += 'L'
        for i in range((x-50)/10):
            result += 'X'
    elif x>=40:
        result += 'XL'
    else :
        for i in range(x/10):
            result += 'X'
    x = x%10
    if x>=9:
        result += 'IX'
    elif x>=5:
        result += 'V'
        for i in range(x-5):
            result += 'I'
    elif x>=4:
        result += 'IV'
    else :
        for i in range(x):
            result += 'I'
    return result

def roman2num(s):
    result,i = 0,0
    while i < len(s):
        if s[i] == 'M' : result += 1000
        if s[i] == 'D' : result += 500
        if s[i] == 'C' :
            n = i+1
            if n<len(s) :
                if s[n] == 'D': result += 400; i+=1
                elif s[n] == 'M': result += 900; i+=1
                else: result += 100
            else: result += 100
        if s[i] == 'L' : result += 50
        if s[i] == 'X' :
            n = i+1
            if n<len(s) :
                if s[n] == 'L': result += 40; i+=1
                elif s[n] == 'C': result += 90; i+=1
                else: result += 10
            else: result += 10
        if s[i] == 'V' : result += 5
        if s[i] == 'I' :
            n = i+1
            if n<len(s) :
                if s[n] == 'V': result += 4; i+=1
                elif s[n] == 'X': result += 9; i+=1
                else: result += 1
            else: result += 1
        i+=1
    return result


if __name__ == '__main__':    
    r1,r2 = 0,0
    f = open("Euler89.txt")
    for s in f:
        r2 += len(num2roman(roman2num(s)))
        r1 += len(s.strip())
    print r1-r2
    pass