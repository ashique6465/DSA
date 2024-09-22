def compress_String(s):
    s = list(s)
    i = 0
    count =  1 
    for j in range(1,len(s)+1):
        if j < len(s) and s[j] == s[j-1]:
            count += 1
        else:
            s[i] = s[j-1]
            i +=1 
            if count > 1 :
                for digit in str(count):
                    s[i] = digit
                    i += 1
            count = 1 
    return "".join(s[:i])
            

s = input()
print(compress_String(s))