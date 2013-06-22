'''
Created on 2013-5-28

@author: lj8175
'''
import math

def listPandigital():
    l = []
    for i in range(1234,9876+1):
        if len(set(str(i))) == 4 and '0' not in str(i):
            for j in range(2,int(math.sqrt(i)+1)):
                if i%j == 0 and '0' not in str(j)+str(i/j) and len(set(str(j)+str(i/j)))==5 and len(set(str(i)+str(j)+str(i/j))) == 9:
                    l.append(i)
                    break
    return l
    

if __name__ == '__main__':
    ret = listPandigital()
    print sum(ret)
    pass