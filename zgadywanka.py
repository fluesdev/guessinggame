# quick and easy game to guess mystery number

import random

secret_number = random.randint(1, 100)
easy_attemps = 10
medium_attemps = 7
hard_attemps = 3 
attemp = 0 

print("Welcome to SecretGame!")
while True:
    diff = int(input("Easy <- 1 \nMedium <- 2 \nHard <-3\nSo what's your pick: "))
    if diff in [1, 2, 3]:
        break 
    else:
        print("Wrong number, try again.")

    
    
#input for user to change difficult lvl 
#easy 10 tries
#medium 7 tries 
#hard 3 tries
if diff == 1:
    while attemp < easy_attemps:
        guess = int(input("Try to guess: "))
        attemp += 1 

        if guess < secret_number:
            print("Your number is lower than secret number")
        elif guess > secret_number:
            print("Your number is higher than my secret number")
        else:
            print(f"Good job! you guessed my secret number in {attemp}!")
            break
    else:
        print(f"You didn't guess my number in max number attemps")

if diff == 2:
    while attemp < medium_attemps:
        guess = int(input("Try to guess: "))
        attemp += 1 

        if guess < secret_number:
            print("Your number is lower than secret number")
        elif guess > secret_number:
            print("Your number is higher than my secret number")
        else:
            print(f"Good job! you guessed my secret number in {attemp}!")
            break
    else:
        print(f"You didn't guess my number in max number attemps")
if diff == 3:
    while attemp < hard_attemps:
        guess = int(input("Try to guess: "))
        attemp += 1 

        if guess < secret_number:
            print("Your number is lower than secret number")
        elif guess > secret_number:
            print("Your number is higher than my secret number")
        else:
            print(f"Good job! you guessed my secret number in {attemp}!")
            break
    else:
        print(f"You didn't guess my number in limited tries")
