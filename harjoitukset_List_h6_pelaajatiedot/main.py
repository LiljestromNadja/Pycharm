"""
List
h6
Esittele merkkijonoja sisältävä lista. Kysy ensimmäiseen paikkaan pelaajan nimi, toiseen seura ja kolmanteen
alkioon pelipaikka.

Tulosta taulukosta arvot seuraavasti:
Ville Peltonen
H
I
F
K
Hyökkääjä

Huomaa että seura on tulostettu merkki kerrallaan.
Käytä for luuppia pelaajatietolistan tulostuksessa
"""

pelaajanTiedot = []
#tai pelaajanTiedot = list()

pelaajanTiedot.append(input("Anna pelaajan nimi: "))
pelaajanTiedot.append(input("Anna pelaajan joukkue: "))
pelaajanTiedot.append(input("Anna pelaajan pelipaikka: "))

for indeksi in range(0, len(pelaajanTiedot)):
    if indeksi == 1:
        for c in pelaajanTiedot[indeksi]:
            print(c)
    else:
        print(pelaajanTiedot[indeksi])