def sumOfsecondLargest(arr,n):
    even = []
    odd = []
    arr.sort()
    for i in range(len(arr)):
        if i % 2== 0:
            even.append(arr[i])
        else :
            odd.append(arr[i])
    even.sort()
    odd.sort()
    print("Even numbers:",even)
    print("Even numbers:",odd)
    sum = 0
    sum += even[-2]
    sum += odd[-2]
    return sum
    
n = 5
arr = [3,4,1,7,9]

print(sumOfsecondLargest(arr,n))
