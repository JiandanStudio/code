import sys
import math

def Pcount(num,count2):
    counttotal=1
    count1=num-count2
    countsub2=1
    countsub1=1
    while num>1:
        counttotal=counttotal*num
        num=num-1
    while count2>1:
        countsub2=countsub2*count2
        count2=count2-1
    while count1>1:
        countsub1=countsub1*count1
        count1=count1-1
    count=counttotal/countsub2/countsub1
    return int(count)

for line in sys.stdin:
    inputvalue=line.strip().split()
    inputvalue=list(map(int,inputvalue))
    steps=inputvalue[0]
    mod = steps%2
    count2=math.floor(steps/2)
    total = 0
    while count2 != 0:
        num=count2+steps-count2*2
        total=total+Pcount(num,count2)
        count2=count2-1
    total=total+1
    print(total)