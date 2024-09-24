def PoetandRhymes(s,d):
    max_match = 0
    best_word = ""
    for word in d:
        if word == s:
            continue
        match_length = 0
        min_len = min(len(s),len(d))
        for i in range(1,min_len+1):
            if word[-i] == s[-i] :
                match_length += 1 
            else:
                break
        if match_length > max_match:
            max_match = match_length
            best_word = word
    return best_word
    
s = input()
d = input().split(",")
print(PoetandRhymes(s,d))