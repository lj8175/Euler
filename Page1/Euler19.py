'''
Created on 2013-5-26

@author: lj8175
'''
import datetime

if __name__ == '__main__':
    begin,end = '19010101','20001231'
    begin = datetime.datetime.strptime(begin,'%Y%m%d')
    oneday=datetime.timedelta(days=1) 
    end = datetime.datetime.strptime(end,'%Y%m%d')
    num = 0
    while(begin<end):
        if begin.weekday() == 6 and begin.day==1:
            num+=1
        begin += oneday
    print num