"""List
h2
Lue käyttäjältä 7 lukua listaan ja tulosta arvot allekkain silmukan avulla
Malliratkaisu
"""

luvut = list()

for indeksi in range(1,8):
    luvut.append(int(input("Anna luku nro " + str(indeksi) + ": ")))

for luku in luvut:
    print(luku)