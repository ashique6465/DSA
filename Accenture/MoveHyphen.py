def MoveHyphen(str):
    n = len(str)
    if str is None:
        return None
    hyphens = []
    non_hyphens = []
    for char in str:
        if char == "-":
            hyphens.append(char)
        else:
            non_hyphens.append(char)
    return ''.join(hyphens + non_hyphens)
str = "Move-Hyphens-to-Front"
print(MoveHyphen(str))

    