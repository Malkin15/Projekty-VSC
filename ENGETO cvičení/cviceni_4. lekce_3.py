vysledek = []
start = 3
stop = 9
delitel = 3

if isinstance (start, int) and isinstance (stop, int) and isinstance (delitel, int):
    print(f"Zadaný rozsah: <{start}, {stop}>")

# Iterace přes hodnoty v intervalu
    for cislo in range(start, stop + 1):
        if cislo % delitel == 0:  # Ověření dělitelnosti
            vysledek.append(cislo)

else:
    print("Zadané vstupy musí být čísla.")

# Výpis výsledku
print(f"Čísla dělitelná {delitel}: {vysledek}")