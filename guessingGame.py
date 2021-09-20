import random
number = random.randint(0,9)
print("Number guessing game")
print("Guess a number between 1 and 9")
chances = 0

while chances < 5:
    guess = int(input("Guess your number:"))
    if guess > number:
        print("You guess is too high. Enter a number that is less than ", guess)
        break
    elif guess < number:
        print("Your guess is too low. Enter a number that is greate than ", guess)

    if guess == number:
        print("YOU WON!!")
    chances += 1
    if not chances < 5:
        print("You lose. The number is", guess)