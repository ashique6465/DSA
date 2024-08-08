def CountPriorElemet(arr):
    if len(arr) == 0:
        return 0
    n = len(arr)
    max_so_far = arr[0]
    count = 1
    for i in range(1,len(arr)):
        if arr[i]>max_so_far:
            count +=1 
            max_so_far = arr[i]
    return count

arr = [3,4,5,8,9]
print(CountPriorElemet(arr))