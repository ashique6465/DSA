import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or Quite(Q): ")
    if(userChoice ==  "Q" ):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("Your number was too small.Take a bigger guess..")
    else:
        print("Your number was too big.Take a small guess..")




print("-----GAME OVER-----")