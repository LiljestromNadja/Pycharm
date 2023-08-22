"""
- Esimerkki kiinteästä parametrimäärästä
- Esimerkki oletusparametreistä
"""

def laske_arvo(rahasumma, korko):
    tuotto = rahasumma + korko
    return tuotto

def laske_korko(rahasumma, korkoprosentti = 2):
    korko = rahasumma * korkoprosentti / 100
    return korko

def laske_kuukaudenkorko(korko):
    kuukaudenkorko = korko / 12
    return kuukaudenkorko

rahamaara = float(input("Anna sijoituksen rahamäärä: "))

korko = laske_korko(rahamaara) #korkoprosentti on tässä oletus eli 2 joka määriteltiin funktiota luodessa
print("Korko oletuskorolla 2% rahasummalla", rahamaara, "on", korko)

uusiKorko = float(input("Anna nyt uusi korkoprosentti: "))
korko2 = laske_korko(rahamaara, uusiKorko)
print("Korko annetulla uudella korkoprosentilla", uusiKorko, "rahasummalle", rahamaara, "on", korko2)

#arvo = laske_arvo(rahamaara) --> tässä tulee virhe, koska pitää olla 2 parametria!
arvo = laske_arvo(rahamaara, korko)
print("Sijoituksen arvo 2% korolla vuoden päästä on:", arvo)
arvoUudellakorolla = laske_arvo(rahamaara, korko2)
print("Sijoituksen arvo uudella ", uusiKorko, "korolla vuoden päästä on", arvoUudellakorolla)

korkoperkk = laske_kuukaudenkorko(korko)
print("Annetulla summalla ja korkoprosentilla {0} korko on kuukaudessa {1:.2f}".format(rahamaara, korkoperkk))

