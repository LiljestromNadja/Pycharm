"""
Set
h1
Tee set, johon arvotaan viisi lukua väliltä 1-10. Samaa lukua ei saa olla kahteen kertaan. Tulosta lopuksi arvotut luvut
"""

import random

luvut = set()

while len(luvut) < 5:
    luku = random.randint(1, 10)

    if luku not in luvut:   #Tämä ei ole pakollinen koska setiin ei voi laittaa samaa arvoa kahteen kertaan
        luvut.add(luku)

for l in luvut:
    print(l)
