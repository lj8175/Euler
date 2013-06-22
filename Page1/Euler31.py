'''
Created on 2013-5-28

@author: joelliu
'''

def numWays():
    moneyList = [1, 2, 5, 10, 20, 50, 100, 200]
    kindList = [1]+[0]*200
    for i in moneyList:
        for j in range(i, 200+1):
            kindList[j] += kindList[j-i]
    return kindList[200]


if __name__ == '__main__':
    print numWays()
    pass