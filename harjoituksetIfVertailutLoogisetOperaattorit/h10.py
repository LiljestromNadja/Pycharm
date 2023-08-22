"""
teema2
h10
Lue käyttäjältä kokonaisluku. Jos luku on väliltä
3-7 tai 9-11 niin tulosta "välissä oli"
Muussa tapauksessa tulosta "ei napsunut väliin"
Mieti miten saisit molemmat ehdot yhteen IFiin.
"""

syote = int(input("Anna kokonaisluku:  "))

if((syote >= 3 and syote <= 7) or (syote >= 9 and syote <=11)):
    print("Välissä oli.")
else:
    print("Ei napsunut väliin..")

luku = int(input("Anna kokonaisluku: "))

""" Opettajan ratkaisu, sulut pythonin tavalla.
if ((luku >= 3) and (luku <= 7)) or ((luku >= 9 ) and (luku <= 11)):
    print("Välissä oli.")
else:
    print("Ei napsunut väliin.")"""