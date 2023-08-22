"""
Teema 4 funktiot osa 2
h5

Tee funktio joka luo setin, jossa on 10 kpl arvottuja lukuja väliltä 1-20.
Kutsu pääohjelmassa ko funktiota vähintään kolme kertaa eli luot kolme set-tyyppistä muuttujaa

Tee yhdistä -funktio, jolle voi tulla n kpl set-tyyppisiä muuttujia ja funktio palauttaa yhdistetyn set-tyyppisen muuttujan.
Eli palautuvassa muuttujassa on vain ne numerot, jotka esiintyvät kaikissa luoduissa seteissä. Lopuksi tulosta -funktio
tulostaa kaikki luvut näytölle pienimmästä suurimpaan allekain.
"""

import random

def luo_set():
    luvut = set()
    while len(luvut) < 10: # Luodaan set
        luku = random.randint(1, 21) # Arvotaan luvut
        luvut.add(luku) #huom, koska set niin add() eikä append()

    return luvut

def yhdista_setit(*args):
    if len(args) == 0:
        return set() #Jos ei yhtään parametria, palautetaan tyhjä set

    yhdistetty = args[0] # Otetaan pohjaksi eka set

    for set in args:
        yhdistetty.intersection(set) # otetaan vain ne luvut jotka molemmissa

    return yhdistetty # Palautetaan kaikkien argumenttisettien leikkaus

def tulosta(yhdistetty):
    lista = list(yhdistetty) # Tehdään setistä lista jotta saadaan se lajiteltua
    lista.sort()
    for i in range(0, len(lista)):
        if i == len(lista)-1: #Huolehditaan ettei rivin loppuun tule pilkkua
            print(lista[i])
        else:
            print(lista[i], end=",")

set1 = luo_set()
set2 = luo_set()
set3 = luo_set()

yhdistetty_set = yhdista_setit(set1, set2, set3)
tulosta(yhdistetty_set)