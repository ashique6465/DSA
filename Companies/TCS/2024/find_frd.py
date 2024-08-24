def Find_frd(d):
    n = len(d)
    if n == 1:
        return 0
    
    l = 0
    count = 0
    for i in range(1,n):
        if d[l] !=d[l-1]:
            count += 1
        
    return count

d = list(map(int,input("Enter the Friends").split(" ")))
print(Find_frd(d))