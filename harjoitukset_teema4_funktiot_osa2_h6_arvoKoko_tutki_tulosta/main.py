"""
Teema 4 funktiot osa 2
h6

Tee ArvoKoko -funktio, jossa arvotaan luku väliltä 25-45. Funktio palauttaa koon. Arvo listaan ArvoLuvut -funktiossa
ko määrä lukuja väliltä -17.3 - 43.3 ja palauta lista. Vie lista parametrina Tutki -funktioon. Siellä käydään taulukko
läpi ja kaikki arvot jotka on väliltä -5.2...+24.6 viedään Tulosta -funktioon ja tulostetaan siellä.
"""

import random

def arvo_koko():
    koko = random.randint(25, 46) #Arvotaan luku väliltä 25-46
    return koko

def arvo_luvut(koko):
    luvut = list()
    for i in range(0, koko-1):
        arvottu = (random.random() * (43.3 - (-17.3))) - 17.3
        luvut.append(arvottu)

    return luvut

def tutki(luvut):
    for luku in luvut:
        if luku >= -5.2 and luku <= 24.6:
            tulosta(luku)

def tulosta(luku):
    print(luku)

koko = arvo_koko()
luvut = arvo_luvut(koko)
tutki(luvut)