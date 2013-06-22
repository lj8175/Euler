'''
Created on 2013-6-21

@author: lj8175
'''

if __name__ == '__main__':
    num = 0
    for i in range(1,10):
        j = 1
        while True:
            if len(str(pow(i,j))) == j:
                num += 1
                #print i,j
            else:
                break
            j += 1
    print num
    pass