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
        # kontrola velkých písmen + neobsahuje čísla a spec. znaky + že slovo má víc než jeden znak
        uppercase_count = sum(1 for word in words if word.isupper() 
        and word.isalpha() and len(word) > 1)
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

# Vytvoření seznamu délek slov bez interpunkce
word_lengths = []
for word in words:
    stripped_word = word.strip(",.!?")  # odstranění interpunkce
    word_length = len(stripped_word)    # zjištění délky slova bez interpunkce
    word_lengths.append(word_length)    # přidání délky slova do seznamu

# Počítání výskytu jednotlivých délek slov
length_counts = {}
for length in word_lengths:
    if length in length_counts:
        length_counts[length] += 1  # zvýšení počtu výskytů pro délku, která už ve slovníku je
    else:
        length_counts[length] = 1   # pokud délka ještě ve slovníku není, přidáme ji s počtem 1

# Zjištění maximální šířky pro jednotlivé sloupce, aby vše bylo zarovnáno
# Zjišťujeme maximální délku textových reprezentací délek slov a výskytů
max_len_width = max(len(str(length)) for length in length_counts)  # např. pro délku slova
max_occurrences_width = 14  # šířka pro sloupec s hvězdičkami
max_count_width = max(len(str(count)) for count in length_counts.values())  # pro sloupec s počty výskytů

# Zobrazení hlavičky a oddělovače s dynamickým zarovnáním pomocí f-stringů
print(f"{'LEN'.rjust(max_len_width)}|{'OCCURENCES'.center(max_occurrences_width)}|{'NR.'.rjust(max_count_width)}")
print(line)

# Zobrazení sloupcového grafu četnosti délek slov
for index, (length, count) in enumerate(sorted(length_counts.items())):
    occurrences = "*" * count  # hvězdičkový graf odpovídající počtu výskytů
    # Dynamický výpis řádků grafu
    print(f"{str(length).rjust(max_len_width)}|{occurrences.ljust(max_occurrences_width)}|{str(count).rjust(max_count_width)}")
