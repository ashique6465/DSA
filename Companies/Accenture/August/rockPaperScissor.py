def RockPaper(a):
    if a == 'rock':
        return "paper"
    elif a == 'scissor':
        return 'rock'
    elif a == 'paper':
        return 'scissor'
    else:
        return False
        

a = input()
print(RockPaper(a))