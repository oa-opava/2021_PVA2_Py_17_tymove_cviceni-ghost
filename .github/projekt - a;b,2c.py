#1-a;b
import re
regex = "[0-9]{6}[0-9]{4}"
rodnecislo = input("Zadej rodné cislo")

def jeSpravne(rodnecislo):
    if (re.fullmatch(regex, rodnecislo)):
        print("správně")
    else:
        print("nesprávně")
