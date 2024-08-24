def findSequence(k,arr):
    l = len(arr)
    start = 0
    max_lenth = 0
    curr_sum = 0
    for i in range(l):
        curr_sum += arr[i]
        while curr_sum >= k and start <= i:
            curr_sum -= arr[start]
            start +=1
        max_lenth = max(max_lenth,i-start + 1)
            
    return max_lenth
k = int(input("Enter the max sum: "))   
arr = list(map(int,input("Enter the sequence: ").split()))

print(findSequence(k,arr))
    
        