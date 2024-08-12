def colorofBallon(arr):
    n = len(arr)
    if n == 0:
        return "No ballon"
    count_color= {}
    for color in arr:
        if color not in count_color:
            count_color[color] = 1
        else:
            count_color[color] +=1
    for color in count_color:
        if count_color[color]%2 != 0:
            return color
    return "All are even"

# arr = ['a','A','b','B','c','C']
arr = []
print(colorofBallon(arr))