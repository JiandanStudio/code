import sys

for line in sys.stdin:
    arrs=line.strip().split(',')
    arrs=list(map(int,arrs))
    arrs.sort()
    print(arrs[int(((len(arrs)+1)/2)-1)])