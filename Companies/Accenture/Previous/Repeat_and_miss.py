def repeat_missing(A):
    n = len(A)
    Expected_sum = (n * (n + 1)) // 2
    arr_sum = sum(A)
    duplicate = arr_sum - sum(set(A))
    missing = duplicate + (Expected_sum - arr_sum)
    return [duplicate,missing]
A = [3,1,2,5,3]
print(repeat_missing(A))