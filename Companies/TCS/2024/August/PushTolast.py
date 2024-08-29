def push_to_last(arr):
    non_zero = []
    zero = []
    for i in range(len(arr)):
        if arr[i] == 0:
            zero.append(arr[i])
        else:
            non_zero.append(arr[i])
    result = non_zero + zero
    return " ".join(map(str, result))
        
arr =list(map(int,input().split()))
print(push_to_last(arr))