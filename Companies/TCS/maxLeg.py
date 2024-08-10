def max_leg(farm):
    max_legs = 0
    for hens,cows in farm:
        total_legs = hens * 2 + cows *4
        if total_legs  > max_legs:
            max_legs = total_legs
    return max_legs
farm = [
    (10,32),
    (23,16),
    (21,89),
    (27,22)
]
print(max_leg(farm))