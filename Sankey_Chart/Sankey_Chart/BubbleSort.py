def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
        for m in range(len(arr)):
                print("%d" % arr[m],end=" ")
        print("\n")


arr = [18,22,91,2,3]

BubbleSort(arr)

# for i in range(len(arr)):
#     print("%d"%arr[i])
