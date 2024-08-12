def minCandies(n,k,s):
    if s > n or s <=0:
        print("INVALID INPUT")
        print("Available: ",n)

    else:
        n -=s
        print("sold: ",s)
        print("Available: ",n)

        if n <= k:
            n = 10
            print("Available: ",n)
    return n
    
    

n = 10
k = 5
s = 3
while True:
    s = int(input("Enter the candies you want: "))
    n = minCandies(n,k,s)
    if n == 0:
        break