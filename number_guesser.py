import random

top_of_range = input("type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("enter a number larger than 0")
        quit()
else:
    print("enter a number")
    quit()

random_number =random.randint(0,top_of_range)
num_guess = 0
while True:
    num_guess += 1
    guess = input("guess a number: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("enter a number")
        continue

    if guess == random_number:
        print("you guessed the correct number")
        break
    elif guess > random_number:
        print("you guessed above the number")
    else:
        print("you guessed below the number")

print("you got it in ", num_guess, "guess(es)")