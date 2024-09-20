def LongestSUb(arr):
    n = len(arr)
    non =[]
    zero = []
    for num in arr:
        if num == 0:
            zero.append(num)
        else:
            non.append(num)
    return non + zero
        
arr = list(map(int,input().split()))
print(LongestSUb(arr))