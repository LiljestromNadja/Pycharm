""" Set {}, lottoarvonta

Kun set on saatu kasaan niin siitä voidaan tehdä lista ja listan avulla esim lajittelu
"""

import random
lkm = 0  # Arvottujen lottonumeroiden määrä

# Arvotaan ns veikkauksen rivi
oikearivi = set()
while True:                     #voidaan myös merkitä while len(oikearivi) < 7
    luku = random.randint(1, 40)
    oikearivi.add(luku)
    if(len(oikearivi) == 7):
        break

print("Veikkauksen rivi: ")
print(oikearivi)

# Tehdään setistä lista, jotta saadaan numerot ok järjestyksessä
jarjestettyVeikkauksenRivi  =list(oikearivi)

jarjestettyVeikkauksenRivi.sort()

# Arvotaan rivejä kunnes 7 oikein
kerrat = 0
while True:
    lkm = 0  # Arvottujen lottonumeroiden määrä
    munrivi = set()  # Tyhjä lista
    while True:
        luku = random.randint(1, 40)
        munrivi.add(luku)
        if (len(munrivi) == 7):
            break

    # Muutetaan listaksi jotta saadaan lajiteltua
    munriviListana = list(munrivi)
    munriviListana.sort()
    print(munriviListana)
    kerrat += 1

    osumat = oikearivi.intersection(munrivi)
    print(osumat)

    if (len(osumat) == 7 ):  #tsekataan tuliko 7 oikein
        break

print("7 osumaa tuli, kun yritetty", kerrat, "kertaa")
