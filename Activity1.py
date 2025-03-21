import random
playing = True
num = str(random.randint(0,10))

while playing:
    guess = input("Guess a number: ")
    if num == guess:
        print("You win the game")
        print("The number was",num)
        break
    else:
        print("Your guess is not right.Try again")