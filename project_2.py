"""
projekt_2.py: druhy projekt do Engeto Online Python Akademie

author: Rostyslav Luzan
email: roluzan@email.cz

"""

import random

space = (40 * "-")

def valid_number(number):
    """Checks if the input is a valid 4-digit number (no leading zero, unique digits).""" 

    return (number.isdigit() and
            len(number) == 4 and 
            number[0] != '0' and
            len(set(number)) == 4)

def generate_number():
    """Generates a random 4-digit number with unique digits and no leading zero."""  

    digits = list(range(1,10))
    first_digit = random.choice(digits)
    digits.remove(first_digit)
    rest_digits = random.sample(digits + [0], 3)
    return str(first_digit) + "".join (map(str,rest_digits))

def play_game():
    """Main loop of the bulls and cows game"""

    name = input("Welcome! What's your name? ")
    secret_number = generate_number()  
    attempts = 0
    
    while True:
        guess = input("Enter a number: ")
        if valid_number(guess):
            attempts += 1
            bulls = sum(1 for secret, guess_digit in zip(secret_number, guess) if secret == guess_digit)
            cows = len(set(secret_number) & set(guess)) - bulls  
            bull_word = "bull" if bulls == 1 else "bulls"
            cow_word = "cow" if cows == 1 else "cows"
            print(f"{bulls} {bull_word}, {cows} {cow_word}")
        
            if bulls == 4:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                print(f"The secret number was: {secret_number}")
                break
        else:
            print("Invalid number. Try again (must be 4 unique digits, not starting with 0).")

print("Hi there!")
print (space)
print("I've generated a random 4 digit number for you.\n"
"Let's play a bulls and cows game!")
print(space)

play_game()