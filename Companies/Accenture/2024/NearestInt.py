def nearestInteger(num,m):
    
    for i in range(num,-1,-1):
        if i%m == 0:
            lower = i
            upper = lower + m
            break
    
    lower_distance = abs(num - lower)
    upper_distance = abs(num - upper)
    if lower_distance < upper_distance:
        return lower
    elif upper_distance < lower_distance:
        return upper
    else:
        return upper
                
num = int(input("Enter the num: "))
m = int(input("Enter the m: "))
print(nearestInteger(num,m))