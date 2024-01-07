import math

DelOrds=[]
delorder = 3

def delNo3(arrs):
    mods = len(arrs)%delorder
    delcount = math.floor(len(arrs)/3)
    tempdels = []
    i=0
    while i < delcount:
        DelOrds.append(arrs[delorder+i*delorder-1])
        tempdels.append(arrs[delorder+i*delorder-1])
        i=i+1
    arrs = list(set(arrs)-set(tempdels))
    for i in range(mods):
        arrs.insert(0,arrs.pop())
    return arrs

def LoopDel(arrs):
    while len(arrs) > 2 :
        arrs=delNo3(arrs)
    i = 2
    while i != 0 :
        DelOrds.append(arrs[i-1])
        i=i-1

arrsnew = [i for i in range(1,501)]

def ReturnPosition(NoID):
    LoopDel(arrsnew)
    print(DelOrds[NoID-1])
    return DelOrds[NoID-1]


ReturnPosition(200)