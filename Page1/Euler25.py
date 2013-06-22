'''
Created on 2013-5-26

@author: lj8175
'''

def fib(x,d={}):
    if len(d) <= 0 : d = {0:0,1:1,2:1}
    l = [{'now':x,'ret':0}]
    if x in d : return d[x]
    while True:
        while l[len(l)-1]['now']-1 not in d:
            l.append({'now':l[len(l)-1]['now']-1,'ret':0})
        l[len(l)-1]['ret'] += d[l[len(l)-1]['now']-1]
        while l[len(l)-1]['now']-2 not in d:
            l.append({'now':l[len(l)-1]['now']-2,'ret':0})
        l[len(l)-1]['ret'] += d[l[len(l)-1]['now']-2]
        d[l[len(l)-1]['now']] = l[len(l)-1]['ret']
        l.pop()
        if len(l) <= 0 : break
    return d[x]

def fibonacci(x,d={}):
    '''
    the largest x can reach 1997
    '''
    if x == 1 or x == 2 : return 1
    if x-2 not in d:
        d[x-2] = fibonacci(x-2,d)
    if x-1 not in d:
        d[x-1] = fibonacci(x-1,d)
    return d[x-1]+d[x-2]

if __name__ == '__main__':
    i = 0
    while len(str(fib(i)))  < 1000:
        i += 1
    print i
