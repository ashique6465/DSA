import math

def lcm(a,b):
    return abs(a*b)//math.gcd(a,b)


def find_drum_beats(n,b):
    visited = [False] * n
    result =1 
    for i in range(n):
        if not visited[i]:
            cyc_len = 0
            current = i
            while not visited[current]:
                visited[current] = True
                current = b[current] -1
                cyc_len +=1
            result = lcm(result,cyc_len)
    return result
n = int(input("Enter the students"))
b = list(map(int,input("Enter the board").split(",")))
print(find_drum_beats(n,b))
        
    