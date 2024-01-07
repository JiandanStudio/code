import sys

for line in sys.stdin:
    shortstr,longstr = line.strip().split()
    count = 0
    for str in shortstr:
        if longstr.find(str) != -1:
            longstr=longstr.replace(str,'-',1)
        else:
            print('false')
            count=1
            break
    if count == 0:
        print('true')