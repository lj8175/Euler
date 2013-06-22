'''
Created on 2013-6-21

@author: lj8175
'''

if __name__ == '__main__':
    i,d = 0,{}
    while True:
        i += 1
        s = ''.join(sorted(list(str(pow(i,3)))))
        if s in d:
            d[s].append(i)
            if len(d[s]) == 5:
                print pow(d[s][0],3)
                break;
        else:
            d[s] = [i]
    pass