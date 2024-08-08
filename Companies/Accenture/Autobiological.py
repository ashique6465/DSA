def FindAutoCount(n):
    if n is None:
        return 0
    seen= {}
    count = 1
    for num in n :
        if num not in seen:
            seen[num] = 1
        else:
            seen[num] +=1
    for i in range(len(n)):
        expected = int(n[i])
        actual  = seen.get(str(i),0)
        if expected != actual:
            return 0             
    return len(seen)
n = "72110"
print(FindAutoCount(n))

    
