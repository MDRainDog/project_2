"""
projekt_2.py: druhy projekt do Engeto Online Python Akademie

author: Rostyslav Luzan
email: roluzan@email.cz

"""


space = (40 * "-")

import random

def valid_number(number):
    return (number.isdigit() and
            len(number) == 4 and 
            number[0] != '0'and
            len(set(number)) == 4)

def generate_number():
    digits = list(range(1,10))
    first_digit = random.choice(digits)
    digits.remove(first_digit)
    rest_digits = random.sample(digits + [0], 3)
    return str(first_digit) + "".join (map(str,rest_digits))

print("Hi there!")
print (space)
print("I've generated a random 4 digit number for you.\n"
"Let's play a bulls and cows game!")
print(space)

secret_number = generate_number()  
attempts = 0
while True:
    guess = input("Enter a number: ")
    if valid_number(guess):
        attempts += 1
        bulls = sum(1 for secret, guess_digit in zip(secret_number, guess) if secret == guess_digit)
        cows = len(set(secret_number) & set(guess)) - bulls  
        print(f"{bulls} bulls, {cows} cows")
        if bulls == 4:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            print(f"The secret number was: {secret_number}")
            break
    else:
        print("The number is incorrect, try again")
        print("- No repeating digits")
        print("- No leading zero")
