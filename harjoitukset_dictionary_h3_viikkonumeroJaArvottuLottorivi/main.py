"""
Dictionary
h3
Tee dictionary, jossa avaimena on viikkonumero 1-52 ja sisältönä arvottu lottorivi eli 7 lukua väliltä 1-40.
Tuplia ei luonnollisestikaan sallita.

Generoi siis aluksi veikkauksen rivit ko viikoille.
Pyydä käyttäjältä hänen rivinsä (siis 7 numeroa väliltä 1-40)
Käy läpi veikkauksen rivit ja tulosta miten olisi lykästänyt annetulla rivillä. Näytä siis viikottainen tulos.
"""

import random

rivitViikottain = dict()

for vk in range(1, 53):
    vkrivi = set()
    while len(vkrivi) < 7:
        nro = random.randint(1, 40)
        vkrivi.add(nro)
    rivitViikottain[vk] = vkrivi

kayttajanRivi = set()
while len(kayttajanRivi) < 7:
    kayttajannro = int(input("Anna rivisi numero 1 - 40: " ))
    if kayttajannro < 1 or kayttajannro > 40:   #jos käyttäjä syöttää arvon joka ei ole välillä 1-40, pyydetään uudestaan
        print("Anna nro väliltä 1-40")
        continue
    if kayttajannro in kayttajanRivi:
        print("Numero on jo rivilläsi")
    else:
        kayttajanRivi.add(kayttajannro)

for i in rivitViikottain:
    print("Viikko", i)
    osumat = kayttajanRivi.intersection(rivitViikottain[i]) # rivit jotka löytyvät kayttajanRivi ja rivitViikottain
    print("\tOsumia oli", len(osumat), "kpl")
    print("\tJa ne olivat", osumat)