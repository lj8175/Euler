'''
Created on 2013-6-4

@author: joelliu
'''

pokerOrder = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, 'T':8, 'J':9, 'Q':10, 'K':11, 'A':12}
handOrder = {0:'High Card', 1:'One Pair', 2:'Two Pairs', 3:'Three of a Kind', 4:'Straight', 5:'Flush',
             6:'Full House', 7:'Four of a Kind', 8:'Straight Flush', 9:'Royal Flush'
             }

def isStraight(pv):
    tmp = pokerOrder[pv[0]]
    for i in range(1,len(pv)):
        if pokerOrder[pv[i]] != tmp+1:
            return False
        else:
            tmp += 1
    return True

def dvc(pvc):
    d = {}
    for i in pvc:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

def whichHandOrder(pv, pc):
    pvd,pcd = dvc(pv),dvc(pc)
    if len(pcd) == 1 and isStraight(pv): 
        return 9 if pv[0] == 'T' else 8
    if 4 in pvd.values() :
        return 7
    if 3 in pvd.values() and 2 in pvd.values():
        return 6
    if len(pcd) == 1:
        return 5
    if isStraight(pv):
        return 4
    if 3 in pvd.values():
        return 3
    tmp = 0
    for i in pvd:
        if pvd[i] == 2 : tmp += 1
    if tmp == 2:
        return 2
    if tmp == 1:
        return 1
    return 0

def p1WinSameOrder(p1vd, p2vd):
    p1m, p2m, p1mv, p2mv = '2', '2', 0, 0
    for i in p1vd:
        if p1vd[i] > p1mv: 
            p1m = i
            p1mv = p1vd[i]
        elif p1vd[i] == p1mv and pokerOrder[i] > pokerOrder[p1m]:
            p1m = i         
    for j in p2vd:
        if p2vd[j] > p2mv: 
            p2m = j
            p2mv = p2vd[j]
        elif p2vd[j] == p2mv and pokerOrder[j] > pokerOrder[p2m]:
            p2m = j
    if pokerOrder[p1m] > pokerOrder[p2m]:
        return True
    elif pokerOrder[p1m] < pokerOrder[p2m]:
        return False
    else:
        p1vd[p1m],p2vd[p2m] = -1,-1
        return p1WinSameOrder(p1vd,p2vd)

def p1Win(p1, p2):
    p1.sort(cmp=lambda x,y:cmp(pokerOrder[x[0]],pokerOrder[y[0]]))
    p2.sort(cmp=lambda x,y:cmp(pokerOrder[x[0]],pokerOrder[y[0]]))
    p1v = [x[0] for x in p1]; p1c = [x[1] for x in p1]
    p2v = [x[0] for x in p2]; p2c = [x[1] for x in p2]
    p1vd,p2vd = dvc(p1v),dvc(p2v)
    if whichHandOrder(p1v, p1c) >  whichHandOrder(p2v, p2c):
        return True
    elif whichHandOrder(p1v, p1c) < whichHandOrder(p2v, p2c):
        return False
    else:
        return p1WinSameOrder(p1vd, p2vd)

if __name__ == '__main__':
    file = open("Euler54.txt")
    num = 0
    for line in file:
        p = line.split()
        flag = p1Win(p[:5], p[5:])
        if flag:
            num += 1
    print num
    pass
    pass