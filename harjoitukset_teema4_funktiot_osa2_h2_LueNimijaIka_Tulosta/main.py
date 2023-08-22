"""
Teema 4 funktiot osa 2
h2

Esittele Lue -funktio, jossa luet henkilön nimen ja iän ja palautat ne pääohjelmaan. Tulosta lopuksi muuttujien
arvot Tulosta -funktiossa
"""

def lue_tiedot():
    nimi = input("Anna nimi: ")
    ika = input("Anna ikä: ")
    return [nimi, ika] # pitää käyttää listaa, koska palautetaan kaksi arvoa

def tulosta(tiedot):
    print("Nimi: ", tiedot[0])
    print("Ikä: ", tiedot[1])

henkilotiedot = lue_tiedot()
tulosta(henkilotiedot)