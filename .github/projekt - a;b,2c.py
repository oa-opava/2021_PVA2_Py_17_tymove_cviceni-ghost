#1
import re
regex = "[0-9]{2}[01-12][0-3][0-9][0-9]{3}[0-9]"
rodnecislo = input("Zadej rodné cislo")

def jeSpravne():
    if re.fullmatch(regex, rodnecislo):
        print("správně")
    else:
        print("nesprávně")
