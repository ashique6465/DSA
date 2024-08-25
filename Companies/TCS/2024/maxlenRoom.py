def findSequence(k,arr):
    n = len(arr)
    l =0
    current_sum = arr[0]
    for j in range(1,n):
        while current_sum >k and l < j:
            current_sum -= arr[l]
            l +=1 
        if current_sum == k:
            return l+1,j
       
        current_sum += arr[j]
    return "No valid sequence found"
k = int(input("Enter the max sum: "))   
arr = list(map(int,input("Enter the sequence: ").split()))

print(findSequence(k,arr))
    