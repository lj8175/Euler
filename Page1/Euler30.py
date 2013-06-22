'''
Created on 2013-5-27

@author: lj8175
'''

def listFifthPowers():
    l,num = [],2
    while True:
        tmp = 0
        for i in str(num):
            tmp += int(i)**5
        if num == tmp: l.append(num)
        if num > 9**5*len(str(num)) : break
        num += 1
    return l
            

if __name__ == '__main__':
    l = listFifthPowers()
    print sum(l)
    pass