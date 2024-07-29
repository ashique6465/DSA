def removeVowels(houses):
    vowels = "a,e,i,o,u"
    remove_char = ""
    result = ""
    for char in houses:
        if char in vowels:
            remove_char += char
        else:
            result += char
    return result
houses = "MnsieklmnopVja"
print(removeVowels(houses))