# -*- coding:utf-8 -*-
'''
Created on 2013年12月13日

@author: lj8175
'''

import re,copy,sys

saveList = [
[131,673,234,103,18],
[201,96,342,965,150],
[630,803,746,422,111],
[537,699,497,121,956],
[805,732,524,37,331]
]

def readSquare():
    fHandler = open("Euler81.txt")
    d = []
    for line in fHandler:
        strlist = re.split(",", line.strip())
        dtmp = []
        for num in strlist:
            dtmp.append(int(num))
        d.append(dtmp)
    return d

def isValidIndex(l,i):
    if i[0]<0 or i[1]<0 : return False
    if i[0]>len(l)-1 or i[1]>len(l[0])-1 : return False
    return True
    pass

def genToLocList(loc, knownList):
    locList, result = [], []
    locList.append([loc[0]-1, loc[1]]) #up
    locList.append([loc[0], loc[1]+1]) #right
    locList.append([loc[0]+1, loc[1]]) #down
    for newLoc in locList:
        if isValidIndex(knownList, newLoc):
            result.append(newLoc)
    return result

def dijkstra(knownList, num):
    dijList = [[sys.maxint for col in range(len(knownList[0]))] for row in range(len(knownList))]
    dijList[num][0] = 0
    sList, memoList, memoL = [[num,0]],[[num,0]],[]
    while sList:
        loc = sList[0]; sList = sList[1:]
        toLocList = genToLocList(loc, knownList)
        for t in toLocList:
            if dijList[t[0]][t[1]] > (dijList[loc[0]][loc[1]] + knownList[loc[0]][loc[1]]):
                dijList[t[0]][t[1]] = dijList[loc[0]][loc[1]] + knownList[loc[0]][loc[1]]
            if t not in memoList:
                memoList.append(t)
                memoL.append(t)
        #warn : find the min value to start
        minValue, tmpLoc = sys.maxint, []
        for tmp in memoL:
            if dijList[tmp[0]][tmp[1]]<minValue:
                minValue = dijList[tmp[0]][tmp[1]]
                tmpLoc = tmp
        if tmpLoc:
            memoL.remove(tmpLoc)
            sList.append(tmpLoc)
    resultList = []
    for t in range(len(knownList)):
        dijList[t][-1]+=knownList[t][-1]
        resultList.append(dijList[t][-1])
    return min(resultList)

if __name__ == '__main__':
    saveList = readSquare();
    resultL = []
    for num in range(len(saveList)):
        knownList = copy.deepcopy(saveList)
        resultNum = dijkstra(knownList, num)
        resultL.append(resultNum)
        #print resultNum, num
    print min(resultL)
