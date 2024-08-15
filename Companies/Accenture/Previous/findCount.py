def findCount(arr,num,diff):
    count = 0
    for i in range(0,len(arr)):
        ab_diff = abs(arr[i] - num)

        if ab_diff <= diff:
            count +=1
            
    if count == 0:
        return -1
    return count
    
arr = [12,3,14,56,77,13]
num = 13
diff = 2
result = findCount(arr,num,diff)
print(result)