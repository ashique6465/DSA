def maxnoGuest(T,E,L):
    cur_guest = 0
    max_till = 0
    for i in range(T):
        cur_guest = cur_guest + E[i] - L[i]
        max_till = max(cur_guest,max_till)
    return max_till



T = int(input("Enter the hours"))
E = list(map(int,input("Entern Entry").split(',')))
L = list(map(int,input("Entern Entry").split(',')))
print(maxnoGuest(T,E,L))