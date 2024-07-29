def differenceofSum(n,m):
    sum_not_div = 0
    sum_div = 0
    for i in range(1,m+1):
        if i%n == 0:
            sum_div += i
        else:
            sum_not_div +=i
    return sum_not_div - sum_div


  

n = 4
m = 20
print(differenceofSum(n,m))
