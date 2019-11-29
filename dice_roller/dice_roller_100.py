from random import randint
repeat = True
while repeat:
    print("You rolled",randint(1,100))
    print("Do you want to roll again?")
    repeat = ("y" or "yes") in input().lower()
