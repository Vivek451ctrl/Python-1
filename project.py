import random

randNumber = random.randint(1, 9)
chances = 0

while chances<5:
    guess = int(input("enter your guess"))
    if randNumber == guess:
        print("congratulations you won!!")
        break
    elif guess<randNumber:
        print("your guess was too low")

    else:
        print("your guess is too high")
    chances = chances+1

if not chances<5:
    print("you lose, the number was:", randNumber)
# print(randNumber)