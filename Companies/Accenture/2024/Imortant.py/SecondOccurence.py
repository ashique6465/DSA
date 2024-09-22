def SecondOccurence(arr):
    if len(arr) < 2:
        return 0
    unique_arr = sorted(set(arr))
    if len(unique_arr) < 2:
        return 0
        
    second_largest = unique_arr[-2]
    return arr.count(second_largest)


arr = list(map(int,input().split()))
print(SecondOccurence(arr))