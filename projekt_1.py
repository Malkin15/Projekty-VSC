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
username = input("Enter your username: ")
password = input("Enter your password: ")
print(line)

# Kontrola přihlašovacích údajů a uvítání
if username in user_data and user_data[username] == password:
    print(f"Welcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print(line)
else:
    print("unregistered user, terminating the program..")
    quit()

### Druhá část programu - výběr textu ###

# Vstup uživatele pro výběr textu
selection = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
print(line)

# Kontrola, zda je vstup číslo
if not selection.isdigit():
    print("Invalid input, terminating the program..")
    quit()

# Převod vstupu na celé číslo a kontrola rozsahu
selection = int(selection)
if 1 <= selection <= len(TEXTS):
    selected_text = TEXTS[selection - 1]  # Indexování od 0
else:
    print(f"Invalid choice. Please select a number between 1 and {len(TEXTS)}, terminating the program..")
    quit()

from collections import Counter  # Import modulu Counter

### Analýza textu ###

# Odstranění přebytečných znaků a vytvoření seznamu slov
words = [word.strip(",.!?") for word in selected_text.split()]

# Předdefinované proměnné pro výsledky analýzy
word_count = 0
titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
numeric_strings = []
numeric_sum = 0
word_lengths = []  # Seznam délek slov pro graf

# Jednotný průchod seznamu slov
for word in words:
    word_count += 1
    word_lengths.append(len(word))  # Ukládání délky slova
    if word.istitle():
        titlecase_words += 1
    elif word.isupper():
        uppercase_words += 1
    elif word.islower():
        lowercase_words += 1
    if word.isdigit():
        numeric_value = int(word)
        numeric_strings.append(numeric_value)
        numeric_sum += numeric_value

# Počítání výskytu jednotlivých délek slov
length_counts = Counter(word_lengths)  # Slovník délka -> počet výskytů

### Výstup analýzy ###
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {len(numeric_strings)} numeric strings.")
print(f"The sum of all the numbers {numeric_sum}")
print(line)

# Zobrazení grafu četnosti délek slov - hlavička
print("LEN".ljust(3), "|", "OCCURENCES".center(14), "|", "NR.".rjust(2), sep="")
print(line)

# Zobrazení sloupcového grafu četnosti délek slov
for length, count in sorted(length_counts.items()):
    print(
        str(length).rjust(3),              # Zarovnání délky slova nalevo
        "|", 
        ("*" * count).ljust(14),           # Vytvoření hvězdičkového grafu
        "|", 
        str(count).ljust(2), sep=""        # Počet výskytů zarovnaný vpravo
    )