"""
teema 4
h6

Tee funktio kysyJaLaske, jossa luetaan käyttäjältä kaksi int-arvoa ja lasketaan niiden osamäärä. Funktio palauttaa
lasketun osamäärän. Tulosta pääohjelmassa osamäärä.
"""

def kysyJaLaske():
    luku1 = int(input("Anna ensimmäinen luku: "))
    luku2 = int(input("Anna toinen luku: "))
    osamaara = luku1 / luku2
    return osamaara

osamaara = kysyJaLaske()

print("Antamiesi lukujen osamäärä on: {0:.4f}".format(osamaara))
