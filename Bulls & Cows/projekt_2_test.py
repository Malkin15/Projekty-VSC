def header():
    """Prints project metadata."""
    project_name = "projekt_2.py"
    project_description = "Druhý projekt do Engeto Online Python Akademie"
    author_name = "Roman Šimík"
    author_email = "simik@sonet.cz"
    print(
        f"""
-----------------------------------------------
{project_name}
{project_description}
Autor: {author_name}
Kontakt: {author_email}
-----------------------------------------------
"""
    )

import random

def welcome():
    print(
        """Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------"""
    )

def game(num_digits):
    # Generate a random 4-digit number as a list of integers
    solution = [random.randint(0, 9) for _ in range(num_digits)]
    print("Solution key (for debugging):", solution)  # Optional: remove this in production
    
    # Initialize the guess counter
    attempts = 0
    
    # Prompt the user only once
    while True:
        attempts += 1
        
        # Get input without repeating "Enter a number:"
        guess_input = input(">>> ")

        # Validate input length and convert to a list of integers
        if len(guess_input) != num_digits or not guess_input.isdigit():
            print(f"Please enter a valid {num_digits}-digit number.")
            continue
        guess = [int(digit) for digit in guess_input]

        # Check for correctness
        if guess == solution:
            print(f"Correct, you've guessed the right number\nin {attempts} guesses!")
            print("-----------------------------------------------")
            print("That's amazing!")
            break
        
        # Calculate bulls and cows
        bulls = sum(1 for i in range(num_digits) if guess[i] == solution[i])
        cows = sum(1 for digit in guess if digit in solution) - bulls
        
        # Print the feedback
        bull_str = "bull" if bulls == 1 else "bulls"
        cow_str = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bull_str}, {cows} {cow_str}")
        print("-----------------------------------------------")

# Spuštění hry
header()
welcome()
game(4)
