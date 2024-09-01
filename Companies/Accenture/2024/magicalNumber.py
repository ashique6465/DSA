def magicalNo(n):
    count = 0
    for i in range(n):
        binary = bin(i)[2:]
        changed = ''
        for c in binary:
            if c == '0':
                changed += '1'
            else :
                changed += '2'
        sum_of_digit =0
        for c in changed:
            sum_of_digit += int(c)
        if sum_of_digit % 2 != 0:
            count +=1
    return count
n = int(input("Enter the n: "))
print(magicalNo(n))