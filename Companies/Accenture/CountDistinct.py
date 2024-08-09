def CountDistinct(arr):
    if arr is None:
        return 0 
    seen = {}
    for i in range(len(arr)):
        if arr[i] not in seen:
            seen[arr[i]] = 1
        else:
            seen[arr[i]] += 1
    return len(seen)



arr = [8,9,5,8,9,7,12]
print(CountDistinct(arr))