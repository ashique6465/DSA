def find_even_odd(arr):
    if arr is None:
        return None
    res = ""
    for num in arr:
        if num % 2 != 0:
            res = res + "Odd"
        else:
            res += "Even"
    return res

arr = [1,2,3,4,5,6]
print(find_even_odd(arr))