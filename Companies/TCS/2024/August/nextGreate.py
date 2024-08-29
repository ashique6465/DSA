def next_greater_element(arr):
    result =[]
    for i in range(len(arr)):
        found = False
        for j in range(i+1,len(arr)):
            if arr[j] > arr[i]:
                result.append(arr[j])
                found = True
                break
        if not found:
            result.append(-1)
    return result

        
arr =list(map(int,input().split()))
print(next_greater_element(arr))