def min_chocolates(arr):
    arr.sort()

    min_diff = arr[-1] - arr[0]
    for i in range(len(arr) - 4):
        min_diff = min(min_diff, arr[i + 4] - arr[i])

    return min_diff

arr = [10, 4, 12, 3, 1]
result = min_chocolates(arr)
print(result)