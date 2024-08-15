def Pr_except_self(arr):
    n = len(arr)
    res =[1] * 4
    prefix = 1
    postfix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= arr[i]
    for i in range(n-1,-1,-1):
        res[i] *= postfix
        postfix *= arr[i]
    return res

    
arr = [1,2,3,4]
print(Pr_except_self(arr))