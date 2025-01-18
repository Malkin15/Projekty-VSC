seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]
delky_slov = {slovo: len(slovo) for slovo in seznam_slov} # slovníková komprehence délky slov
print(delky_slov)