def countRate(r,unit,arr):
    n = len(arr)
    

    if n == 0:
        return -1
   
    total_food_needed = r * unit
    current_food = 0
    for i in range(len(arr)):
        current_food += arr[i]
        if current_food >= total_food_needed:
            return i + 1
    
    return 0 
arr = [2,8,3,5,7,4,1,2]
r = 7
unit = 2
print(countRate(r,unit,arr))