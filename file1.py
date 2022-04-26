import random
number = random.randint(0,9)
chances = 0

while chances < 5:
    guess = int(input("Guess a number between 0 to 9: "))
    print("You have", 4-chances, "tries left")
    chances = chances + 1
    if guess > number:
        print("Your guess is greater than the number")
    elif guess < number:
        print("Your guess is less than the number")
    elif guess == number:
        print("CONGRATULATIONS YOU WON")
        chances = chances + 10
    
if chances > 5 and chances < 9:
    print("You Lose... The number is", number)