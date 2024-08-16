def ElevationElement(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    for i in range(n-1):
        if arr[i+1] < arr[i]:
            return arr[i]
    return arr[-1]
    
arr = list(map(int,input("Enter the kilometer: ").split(',')))
print(ElevationElement(arr))