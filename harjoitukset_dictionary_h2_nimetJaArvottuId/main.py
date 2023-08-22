"""
Dictionary
h2
Lue käyttäjältä henkilön nimiä. LOPPU päättää nimien syötön. Arvo henkilölle ID, joka on luku väliltä 1000-20000.
Kahdella henkilöllä ei voi siis olla samaa IDn arvoa eli jos arvottu ID löytyy jo, niin on arvottava uusi ID. Vie henkilön
nimi+ID dictionaryyn ja tulosta kaikkien tiedot lopuksi sieltä.
"""

import random

nimet = dict()

while True:
    nimi = input("Anna nimi: ")
    if nimi.upper().strip() == "LOPPU":
        break
    while True:
        iidee = random.randint(1000, 20000)
        if iidee not in nimet:
            nimet[iidee] = nimi
            break

for iidee in nimet:
    print(iidee, nimet[iidee])
