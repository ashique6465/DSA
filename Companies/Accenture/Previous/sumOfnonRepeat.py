def sum_of_noRepeat(arr):
    E_count = {}
    for element in arr:
        if element in E_count:
            E_count[element] += 1
        else:
            E_count[element] = 1
    
    sum_of_unique =  0
    for element, count in E_count.items():
        if count ==1:
            sum_of_unique += element
    return sum_of_unique

arr = [2,4,3,5,2,9,3]
print(sum_of_noRepeat(arr))