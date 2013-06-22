'''
Created on 2013-5-30

@author: joelliu
'''

def isPandigital(x):
    l,i =[], 1
    while True:
        if len(str(x*i)) == len(set(str(x*i))):
            l.append(str(x*i))
        else: break
        s = ''.join(l)
        if '0' in s: break
        tmp = 0
        for j in l: tmp += len(j)
        if tmp>9 : break
        if tmp==len(set(s)) :
            if tmp == 9: return l
        else: break
        i += 1    
    return []
            

if __name__ == '__main__':
    num = 0
    for i in range(10000):
        ret = isPandigital(i)
        if len(ret) != 0:
            #print i, ret
            if (int(''.join(ret))) > num:
                num = int(''.join(ret))
    print num
    pass