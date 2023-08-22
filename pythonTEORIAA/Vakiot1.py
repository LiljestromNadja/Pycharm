"""
Vakiot

Pythonissa ei ole perinteistä tyyliä määritellä vakioita. Niinpä se tyypillisesti tehdään määrittelemällä
funktio, joka palauttaa vakioarvon. Muitakin tapoja on. Vakiofunktiot kirjoitetaan AINA ISOILLA KIRJAIMILLA, niin
kaikki tietävät koodia lukiessaan, että kyseessä on vakio. VAKION ARVO EI MUUTU EIKÄ SITÄ VOI MUUTTAA MÄÄRITTELYN JÄLKEEN.
"""

def MAX_IKA():
    return 120
def MIN_IKA():
    return 0

print("Annapa ikä: ", end=' ')
ika = int(input())
if(ika >= MIN_IKA() and ika <= MAX_IKA()):
    print("Ikä ok")
else:
    print("Ikä ei kelpaa, sen täytyy olla väliltä 0-120")