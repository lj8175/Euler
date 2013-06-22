'''
Created on 2013-5-27

@author: joelliu
'''

def unitFraction(x):
    if x <= 1 : return 'x should big than 1'
    s,l,ret = 1,[1],['0','.']
    while True:
        s *= 10
        while s<x: 
            s*=10
            ret.append('0')
        ret.append(str(s/x))
        s = s%x
        if s == 0 : break
        elif s in l : 
            ret.insert(l.index(s)+2, '(')
            ret.append(')')
            break
        l.append(s)
    r = ''
    for i in ret:
        r += i
    return r
        


if __name__ == '__main__':
    largest,ret = 0, 0
    for i in range(1000):
        u = unitFraction(i)
        if ')' in u and '(' in u and u.index(')') - u.index('(') > largest:
            largest = u.index(')') - u.index('(') - 1
            ret = i
    print ret