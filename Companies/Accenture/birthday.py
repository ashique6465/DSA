def Max_cut_cake(n):
    M =  1000000007
    if  n == 0:
        return 1
    return((n*(n+1)//2 + 1)%M)

n = int(input("Enter the cuts: "))
print(Max_cut_cake(n))