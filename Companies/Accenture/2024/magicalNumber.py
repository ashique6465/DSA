def findMagicalNumber(n):
    count = 0
    for i in range(1,n):
        binary= bin(i)[2:]
        changed_diget = ''.join('1' if ch == '0' else '2' for ch in binary)
        sum_of_digt = sum(int(ch) for ch in changed_diget)

        if sum_of_digt % 2 != 0:
            count +=1
    return count
n = 4
print(findMagicalNumber(n))