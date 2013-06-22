'''
Created on 2013-5-25

@author: lj8175
'''

def strNum(x):
    if x > 1000 or x < 1:
        return "x should be over 0 and not over 1000"
    d ={
        1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 
        11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
        20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety',
        100:'hundred', 1000:'thousand'        
        }
    if x/1000 > 0:
        return d[x/1000]+d[1000]
    ret = ''
    if x/100 > 0:
        ret += d[x/100]+d[100]
        x = x%100
        if x: ret += 'and'
    if x in d : ret += d[x]
    elif x: 
        ret += d[x-x%10]
        ret += d[x%10]
    return ret

if __name__ == '__main__':
    num = 0
    for i in range(1,1001):
        num += len(strNum(i))
    print num
    pass