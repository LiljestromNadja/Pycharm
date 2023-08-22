"""
Teema 4
h3

Tee funktio kysyNimi, joka kysyy käyttäjältä nimen ja palauttaa sen. Tee funktio kysySyntymavuosi, joka
kysyy käyttäjältä syntymävuoden ja palauttaa sen. Tee funktio laskeIka, joka ottaa parametrikseen syntymävuoden, laskee
henkilön iän (vuonna 2021) ja palauttaa sen. Tee funktio tulosta, joka ottaa parametrikseen nimen ja iän ja tulostaa
tiedot näytölle.
"""

def kysyNimi():
    nimi = input("Anna nimi: ")
    return nimi

def kysy_syntymavuosi():
    svuosi = int(input("Anna syntymävuosi: "))
    return svuosi

def laskeIka(syntymavuosi):
    ika = 2021 - syntymavuosi
    return ika

def tulosta(nimi, ika):
    print(nimi, "olet", ika, "vuoden ikäinen")

nimi = kysyNimi()
svuosi = kysy_syntymavuosi()
ika = laskeIka(svuosi)
tulosta(nimi, ika)