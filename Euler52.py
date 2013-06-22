'''
Created on 2013-6-1

@author: lj8175
'''

if __name__ == '__main__':
    i,flag = 1,True
    while flag:
        i += 1
        lr = []
        for j in range(1,6):
            lr.append(sorted(list(str(i*(j+1)))))
        if len(set(lr[-1])) != len(set(lr[0])) : continue
        for k in lr:
            if lr[-1] != k: flag=False;break
        if flag: flag = False;print i#,lr
        else : flag = True
    pass