def LongestSUb(arr):
    n = len(arr) 
    lis = [1] * n
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if arr[i] < arr[j]:
                lis[i] = max(lis[i], 1 + lis[j])
    return max(lis)
arr = list(map(int,input().split()))
print(LongestSUb(arr))