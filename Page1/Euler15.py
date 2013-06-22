'''
Created on 2013-5-25

@author: lj8175
'''

def numPaths(x,y, d={}):
    if x == 0 or y == 0 :
        return 1
    p1key, p2key = str(x-1)+":"+str(y), str(x)+":"+str(y-1)
    if p1key not in d:
        d[p1key] = numPaths(x-1, y, d)
    if p2key not in d:
        d[p2key] = numPaths(x, y-1, d)
    return d[p1key]+d[p2key]

        
            

if __name__ == '__main__':
    #d = {}
    print numPaths(20, 20)
    pass