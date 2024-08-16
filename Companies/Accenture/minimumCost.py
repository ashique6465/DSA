def MinCost(s1,s2):
    s1_count = {}
    for char in s1:
        if char not in s1_count:
            s1_count[char] = 1
        else:
            s1_count[char] +=1
    
    s2_count = {}
    for char in s2:
        if char not in s2_count:
            s2_count[char] = 1
        else:
            s2_count[char] +=1
    cost = 0
    for char in s2_count:
        if s2_count[char] > s1_count.get(char,0):
            cost += s2_count[char] - s1_count.get(char,0)
    return cost

             
               

s1 = input("Enter the first string")
s2 = input("Enter the second string")
print(MinCost(s1,s2))