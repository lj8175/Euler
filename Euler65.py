'''
Created on 2013-7-8

@author: lj8175

n[k] = c[k]*n[k-1] + n[k-2]
'''


if __name__ == '__main__':
    a, b = 2, 3
    for i in range(3,101):
        c = 2*(i/3) if (i%3==0) else 1
        x = c*b + a
        a, b = b, x
    print reduce(lambda m,n:int(m)+int(n), str(x))
    pass