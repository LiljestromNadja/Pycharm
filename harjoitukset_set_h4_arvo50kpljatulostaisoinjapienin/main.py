"""
Set
h4
Tee kaksi settiä johon arvot 50 kpl lukuja välillä 1-1000. Sen jälkeen tulosta suurin ja pienin luku joka esiintyy
molemmissa seteissä.
"""

import random

luvut1 = set()
luvut2 = set()

while len(luvut1) < 50:
    luku = random.randint(1, 1000)
    luvut1.add(luku)

while len(luvut2) < 50:
    luku = random.randint(1, 1000)
    luvut2.add(luku)

yhdistetty = luvut1.intersection(luvut2)    # intersection Kerää luvut jotka ovat setissä 1 JA setissä 2

print("Luvut jotka ovat molemmissa seteissä: ")
for l in yhdistetty:
    print(l)

if len(yhdistetty) > 0:
    print("Yhteinen minimi:", min(yhdistetty))
    print("Yhteinen maksimi:", max(yhdistetty))