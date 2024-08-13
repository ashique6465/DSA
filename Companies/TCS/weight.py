def weight_time(n):
    
    if n == 0:
        return "Time Estimated: 0 minutes"
    if n <= 2000:
        return "Time Estimated: 25 minutes"
            
    elif n > 2000 and n <= 4000:
        return "Time Estimated: 35 minutes"
            
    elif n >4000 and n <= 7000:
        return "Time Estimated: 45 minutes"
        
    elif n > 7000:
        return "OVERLOAD"
    else:
        return "INVALID INPUT"
    
n = int(input("Enter the Weight: "))
print(weight_time(n))

