def RatCount(arr,r,unit):
    if arr is None or n==0:
        return -1
    current_food = 0
    total_food_needed = r * unit
    for i in range(len(arr)):
        current_food += arr[i]
        if current_food >= total_food_needed:
            return i + 1
    return 0

 


arr = list(map(int,input("Enter the elements: ").split()))
r = int(input("Enter the no. of rat: "))
unit = int(input("Enter the required food: "))
print(RatCount(arr,r,unit))