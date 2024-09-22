def cal_Bio(n,k):
    if k == 0 or k ==n:
        return 1 
    if k > n:
        return 0
        
    return cal_Bio(n-1,k-1) + cal_Bio(n-1,k)
n = int(input())
k = int(input())
print(cal_Bio(n,k)) 