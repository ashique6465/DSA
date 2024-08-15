def ProductSmallestPair(sum,arr): 
    n = len(arr)
    if n == 0 or n < 2:
        return -1
    arr.sort()
    
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] + arr[j] <= sum:
                return arr[i] * arr[j]
            
    return 0
         



arr = [9, 8, 3, -7 ,-7,3 ,9]
sum = 4
print(ProductSmallestPair(sum,arr))