# quick and easy game to guess mystery number

import random

secret_number = random.randint(1, 100)
max_attemps = 10 
attemp = 0 


print("Hello to my game try to guess number that i picked in my mind")


while attemp < max_attemps:
    guess = int(input("Try to guess: "))
    attemp += 1 

    if guess < secret_number:
        print("Your number is lower than secret number")
    elif guess > secret_number:
        print("Your number is higher than my secret number")
    else:
        print(f"Good! job your guesses my secret number in {attemp}!")
        break
else:
    print(f"You didn't guess my number in max number attemps")

