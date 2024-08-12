def minSizeArray(arr,x):
    i = 0
    while i < len(arr):
        if arr[i] == x and x%2 ==0:
            arr.pop(i)
        elif arr[i] == x and arr.count(x) > 1:
            arr.pop(i)
        else:
            i +=1
    return len(arr)

    
x = 4
arr = [3,7,9,10]
print(minSizeArray(arr,x))