import random

def header():
    """Vypíše metadata projektu."""
    project_name = "projekt_2.py"
    project_description = "Druhý projekt do Engeto Online Python Akademie"
    author_name = "Roman Šimík"
    author_email = "simik@sonet.cz"
    line = "-" * 47  # Dynamicky vytvoří čáru o délce 47 znaků
    print(
        f"""
{line}
{project_name}
{project_description}
Autor: {author_name}
Kontakt: {author_email}
{line}
"""
    )

def welcome():
    """Vypíše úvodní zprávu ke hře s aktualizovanými pravidly."""
    line = "-" * 47
    print(
        f"""Hi there!
{line}
I've generated a random 4-digit number for you.
Each digit is unique, and the number doesn't start with 0.
Let's play a bulls and cows game.
{line}"""
    )

def generate_unique_number(num_digits):
    """Vygeneruje náhodné číslo s unikátními číslicemi, které nezačíná nulou."""
    while True:
        digits = random.sample(range(1, 10), 1) + random.sample(range(0, 10), num_digits - 1)
        if len(set(digits)) == num_digits:  # Zkontroluje unikátnost
            return digits

def validate_input(guess_input, num_digits, line):
    """Zkontroluje, zda je vstup od uživatele platný."""
    if (
        len(guess_input) != num_digits or  # Délka není správná
        not guess_input.isdigit() or       # Obsahuje nečíselné znaky
        guess_input[0] == '0' or           # Začíná nulou
        len(set(guess_input)) != num_digits  # Obsahuje duplicity
    ):
        print(
            f"Invalid input! Make sure your number:\n"
            f"- Has exactly {num_digits} digits.\n"
            f"- Contains no repeated digits.\n"
            f"- Does not start with 0.\n"
            f"- Contains only numerical digits.\n{line}"
        )
        return False
    return True

def calculate_bulls_and_cows(guess, solution):
    """Spočítá počet bulls (býků) a cows (krav)."""
    bulls = sum(1 for i in range(len(guess)) if guess[i] == solution[i])
    cows = sum(1 for digit in guess if digit in solution) - bulls
    return bulls, cows

def game(num_digits):
    """Hlavní herní smyčka pro Bulls and Cows."""
    # Vygeneruje náhodné číslo s unikátními číslicemi
    solution = generate_unique_number(num_digits)

    # Debugging: možnost zakomentovat následující řádek v produkčním prostředí
    print("Solution key (for debugging):", solution)  

    # Počítadlo pokusů
    attempts = 0
    line = "-" * 47

    while True:
        attempts += 1

        # Získá vstup od uživatele
        guess_input = input(">>> ")

        # Validace vstupu
        if not validate_input(guess_input, num_digits, line):
            continue

        # Transformuje platný vstup na seznam čísel
        guess = [int(digit) for digit in guess_input]

        # Kontrola, zda uživatel zadal správné číslo
        if guess == solution:
            print(
                f"Correct, you've guessed the right number\n"
                f"in {attempts} guesses!\n"
                f"{line}\n"
                "That's amazing!"
            )
            break

        # Výpočet bulls and cows
        bulls, cows = calculate_bulls_and_cows(guess, solution)

        # Výběr správného tvaru slova
        bull_word = "bull" if bulls == 1 else "bulls"
        cow_word = "cow" if cows == 1 else "cows"

        # Vypíše zpětnou vazbu pro uživatele
        print(f"{bulls} {bull_word}, {cows} {cow_word}\n{line}")

# Spuštění programu
header()  # Vypíše metadata projektu
welcome() # Vypíše úvodní zprávu ke hře
game(4)   # Spustí hru
