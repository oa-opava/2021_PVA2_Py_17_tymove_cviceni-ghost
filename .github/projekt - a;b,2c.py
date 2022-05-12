#1
import re
regex = "[0-9]{2},[01-12],[01-31],[0-9]{3},[0-9]"
rodnecislo = input("Zadej rodné cislo")

if re.fullmatch(regex, rodnecislo):
    print("splňuje")
else:
    print("nesplňuje")
