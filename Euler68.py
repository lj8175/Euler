'''
Created on 2013-12-9

@author: joelliu
'''

import itertools;

if __name__ == '__main__':
    maxgon5 = 0
    for l in itertools.permutations(range(1,11)):
        strList, s = [], []
        s.append(l[5]+l[0]+l[1]); strList.append("%s%s%s"%(l[5],l[0],l[1]))
        s.append(l[6]+l[1]+l[2]); strList.append("%s%s%s"%(l[6],l[1],l[2]))
        s.append(l[7]+l[2]+l[3]); strList.append("%s%s%s"%(l[7],l[2],l[3]))
        s.append(l[8]+l[3]+l[4]); strList.append("%s%s%s"%(l[8],l[3],l[4]))
        s.append(l[9]+l[4]+l[0]); strList.append("%s%s%s"%(l[9],l[4],l[0]))
        if s[0] == s[1] and s[1] == s[2] and s[2] == s[3] and s[3] == s[4]:
            gon1minIndex = l.index(min(l[5:]))-5;
            #print l, gon1minIndex
            gon5 = ''.join(strList[gon1minIndex:]+strList[:gon1minIndex]);
            if len(gon5) == 16 and int(gon5) > maxgon5:
                maxgon5 = int(gon5)
            #break
    print maxgon5
    pass