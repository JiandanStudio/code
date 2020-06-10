import math
arr = [i for i in range(1, 3001)]
i = 3
while i != 1:
    lenl = len(arr)
    lenc = math.floor(len(arr)/3)
    delarr = []
    if i != 1:
        j = 0
        while j < (lenc):
            delarr.append(arr[i+j*3-1])
            j = j+1
    else:
        False
    arr = list(set(arr) - set(delarr))
    i = 3 - lenl % 3
arr.remove(1)
print(len(arr))
print(arr[180])
