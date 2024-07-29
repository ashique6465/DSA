def LargerSmallSum(arr):
    n = len(arr)
    if n == 0 or n <=3:
        return 0
    even_element = []
    odd_element = []
    for i in range(n):
        if i%2 == 0:
            even_element.append(arr[i])
        if i %2 != 0:
            odd_element.append(arr[i])
    even_element.sort()
    odd_element.sort()

    if len(even_element) < 2 or len(odd_element) < 2:
        return 0
    second_largest = even_element[-2]
    second_smallest = odd_element[1]
    return second_largest + second_smallest








arr = [3,2,1,7,5,4]
print(LargerSmallSum(arr))