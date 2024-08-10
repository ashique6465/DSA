def Rotate_string(str,k):
    words = str.split()
    n = len(str)
    k = k%n
    rotated_words = words[-k:] + words[:-k]
    return " ".join(rotated_words)
k = 3
str = "am i going to school"
print(Rotate_string(str,k))