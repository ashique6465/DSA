def TotalDays(arr):
    n = len(arr)
    if n == 0 or n ==1:
        return 0
    count = 0
    for i in range(n-1):
        if arr[i+1] < arr[i]:
            count +=1
    return count
arr =list(map(int,input("Enter the stock price: ").split(',')))
print(TotalDays(arr))
