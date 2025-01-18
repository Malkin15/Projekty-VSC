veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
samohlasky = "aeiouáéíóú"
souhlasky = "bcčdďfghjklmnňprřsštťvzžcdž"
vysledek = {samohlasky: 0, souhlasky: 0}

# Iterace přes zadanou proměnnou 'veta'
for pismeno in veta:
    if not pismeno.isalpha():
        continue
 # .. pokud je převedený znak mezi hodnotami samohlásek
    elif pismeno.lower() in samohlasky:
        vysledek[samohlasky] += 1
# .. pokud je převedený znak mezi hodnotami souhlásek  
    elif pismeno.lower() in souhlasky:
        vysledek[souhlasky] += 1

# Vypiš závěrečný výstup v podobě celkového počtu samohlásek a souhlásek
print(f"Počet souhlásek: {vysledek[souhlasky]} | Počet samohlásek: {vysledek[samohlasky]}")