def houseCanClimb(arr):
    count = 0
    for num in arr:
        if num % 3 == 0:
            count +=1
    return count


arr = list(map(int,input("Enter the Houses: ").split(' ')))
print(houseCanClimb(arr))