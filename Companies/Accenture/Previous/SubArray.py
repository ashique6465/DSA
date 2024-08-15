def SubArray(arr,k):
    n = len(arr)
    if arr is None or n < k or k<= 0:
        return None
    min_sum = float('inf')
    min_subarray = []
    for i in range(n-k + 1):
        SubArray = arr[i:i+k]
        current_sum = sum(SubArray)
        if current_sum < min_sum:
            min_sum = current_sum
            min_subarray = SubArray
    return min_subarray

    

    
arr = [3,2,1,-4,6,3,1]
k = 3
print(SubArray(arr,k))


