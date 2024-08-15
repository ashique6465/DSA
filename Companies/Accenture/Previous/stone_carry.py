def stoneCarry(M,N,common_stone):
    mars_weight = list(range(1,M+1))
    earth_weight = common_stone
    mars_set = set(mars_weight)
    earth_set = set(earth_weight)
    unique_mars_weight = list(mars_set-earth_set)
    unique_mars_weight.sort()
    total_weight = 0
    Stone_selected = 0
    for weight in unique_mars_weight:
        if total_weight + weight <=M:
            total_weight += weight
            Stone_selected += 1
        else:
            break
    return Stone_selected
        


M = int(input("Enter the capasity: "))
N = int (input("Enter the common stones"))
common_stone  = list(map(int,input("Enter the stones from earth").split()))
output = stoneCarry(M,N,common_stone)
