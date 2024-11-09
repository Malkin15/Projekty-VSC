    ### Hlavička ###
# Proměnné s údaji
project_name = "projekt_1.py"
project_description = "první projekt do Engeto Online Python Akademie"
author_name = "Roman Šimík"
author_email = "simik@sonet.cz"
line = "-" * 40

# Vstupní text pro analýzu
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
    ### první část programu - ověření uživatelů ###

# databáze uživatelů a hesel - slovník
user_data = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "lizz": "pass123"
}
# Vyžádání si přihlašovacího jména a hesla
print(f"$ python {project_name}")
username = input("Enter your username: ")
password = input("Enter your password: ")
print(line)

# Kontrola přihlašovacích údajů a uvítání
if username in user_data and user_data[username] == password:
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print(line)
else:
    print("unregistered user, terminating the program..")
    quit()

    ### druhá část programu - výběr z textu ###

# Vstup uživatele pro výběr textu
selection = input("Enter a number btw. 1 and 3 to select: ")
print(line)

# Kontrola, zda je vstup číslo a zda je v platném rozsahu
if selection.isdigit():
    selection = int(selection)
    if 1 <= selection <= 3:
        selected_text = TEXTS[selection - 1]

       # Rozdělení textu na slova pro analýzu
        words = selected_text.split()

        # Analýza textu uložená do proměnných
        word_count = len(words)
        titlecase_count = sum(1 for word in words if word.istitle())
        uppercase_count = sum(1 for word in words if word.isupper())
        lowercase_count = sum(1 for word in words if word.islower())
        numeric_count = sum(1 for word in words if word.isdigit())
        numeric_sum = sum(int(word) for word in words if word.isdigit())

        # Výstup analýzy
        print("There are", word_count, "words in the selected text.")
        print("There are", titlecase_count, "titlecase words.")
        print("There are", uppercase_count, "uppercase words.")
        print("There are", lowercase_count, "lowercase words.")
        print("There are", numeric_count, "numeric strings.")
        print("The sum of all the numbers", numeric_sum)
        print(line)

# Když se zadá špatný formát nebo rozsah
    else:
        print("Invalid input! terminating the program..")
else:
    print("Selection have to be number! terminating the program..")

    ### třetí část programu - grafy ###