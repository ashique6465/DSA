def SecondLargest(arr):
    arr.sort()
    if len(arr)  < 2:
        return 0
    unique = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            unique.append(arr[i])
    unique.append(arr[-1])
    count = 0
    if len(unique) < 2:
        return 0
    SecondLargest = unique[-2]
    for num in arr:
        if num == SecondLargest:
            count +=1
    return count

arr = list(map(int,input("Enter array: ").split()))
print(SecondLargest(arr))
