"""
Set
h2
Tee kaksi listaa, johon arvot 10 lukua väliltä 10-50. Sama luku voi esiintyä useampaan kertaan. Tee niistä set,
jossa luvut jotka on jommassa kummassa tai molemmissa listoissa. Tulosta setin sisältö lopuksi
"""

import random

numerot1 = list()
numerot2 = list()

for i in range(1, 11):
    eka = random.randint(10, 50)
    toka = random.randint(10, 50)
    numerot1.append(eka)        #Viedään listaan
    numerot2.append(toka)       #Viedään listaan

print("Ekan listan sisältö: ")
for l in numerot1:
    print(l)

print("Tokan listan sisältö: ")
for l in numerot2:
    print(l)

yhdistetty = set()
for l in numerot1:
    yhdistetty.add(l)

for l in numerot2:
    yhdistetty.add(l)

print("Yhdistetty lukujoukko, ei duplikaatteja")
for l in yhdistetty:
    print(l)
