'''
Created on 2013-12-18

@author: joelliu
'''

#http://www.marmet.org/louis/sumprod/index.html
#http://www.mathblog.dk/project-euler-88-minimal-product-sum-numbers/

import math,copy

def listMul(l):
    result = 1
    for i in l:
        result *= i
    return result

def combineList(num,maxValue):
    li=[2]+[2]*(num-1)
    l = [copy.deepcopy(li)]
    while li[0]<=li[1] and listMul(li) <= maxValue:
        li[-1] += 1
        if listMul(li) <= maxValue:
            l.append(copy.deepcopy(li))
        else:
            for x in range(1,len(li)+1):
                li[-x]+=1
                for y in range(-x,0):
                    li[y] = li[-x]
                if listMul(li) < maxValue:
                    l.append(copy.deepcopy(li))
                    break
        #print li
    return l

if __name__ == '__main__':
    known, l ,resultDict = 12000, [], {}
    for i in range(2,int(math.sqrt(known*2))+1):
        l+=combineList(i,2*known+1)
    #print len(l)#, l
    for i in l:
        num = listMul(i) - sum(i) + len(i)
        if num > known : continue
        if num not in resultDict :
            resultDict[num] = listMul(i)
        elif listMul(i) < resultDict[num]:
            resultDict[num] = listMul(i)
    s = set()
    for i in range(2, known+1):
        s.add(resultDict[i])
    print sum(s)#, s
            
    pass