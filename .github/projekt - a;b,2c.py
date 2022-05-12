#1
import re
regex = "[00-99,01-12,01-31,1-9{3},0-9]"
rodnecislo = input("Zadej rodné cislo")

if(re.fullmatch(regex, rodnecislo)):
    print("splňuje")
else:
    print("nesplňuje")


#2
jeSpravne =