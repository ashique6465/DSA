def Calculate(m,n):
    sum_of_num = 0
    for i in range(m,n):
        if i % 3 == 0 and i %5 ==0:
            sum_of_num += i
    return sum_of_num


m = int(input("Enter the first digit: "))
n = int(input("Enter the second digit: "))
print(Calculate(m,n))