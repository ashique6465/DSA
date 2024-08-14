def maxFavSong(S,k):
    n = len(S)
    if S is None:
        return None
    if n < k :
        return 0
    max_count = count_a = S[:k].count('a')

    for i in range(1,n-k+1):
        if S[i-1] == 'a':
            count_a -= 1
        if S[i+k-1] == 'a':
            count_a +=1
        max_count = max(max_count,count_a)
    return max_count

S = "Abcaca"
k =3
print(maxFavSong(S,k))
