import random
number = random.randint(0,9)
print("Number guessing game")
print("Guess a number between 1 and 9")
guess = input("Guess your number:")
chances = 5

while chances < 5:
    if guess > number:
        print("You guess is too high. Enter a number that is less than "+ number)
        print(guess)
        chances = chances-1
    elif guess < number:
        print("Your guess is too low. Enter a number that is greate than "+number)
        print(guess)
        chances = chances-1

    if guess == number:
        print("YOU WON!!")

    if not chances < 5:
        print("You lose. The number is", number)