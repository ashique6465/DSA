def CountNegative(temperatures):
    n = len(temperatures)
    count = 0
    for i in range(n):
        if temperatures[i] < 0:
            count +=1
        
    return count

temperatures = 9 , -1, 8, -1 ,3, -4, 8
print(CountNegative(temperatures))