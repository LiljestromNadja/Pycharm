"""
Teema 3 kt 2

Kysy käyttäjältä montako lukua arvotaan.
Jos käyttäjä syöttää arvon < 1 tulostuu "Virhe!".
Tee lista ja arvo siihen em määrä lukuja väliltä 0-20.
Vain PARILLISET luvut sallitaan.
Jos arvottiin pariton luku niin sen tilalle on arvottava uusi luku.
Tulosta luvuista suurin ja pienin samalle riville.
Ja lopuksi tulosta arvotut luvut yhdelle riville pilkulla erotettuna.
Huomaa että viimeisen luvun jälkeen ei tule pilkkua

Esimerkkiajo

Montako lukua arvotaan: 3
Suurin: 6 ja pienin: 0
4,0,6
"""

import random
arvottavat = []
#rajat
suurinLuku = -1
pieninLuku = 21

montakoLukua = int(input("Montako lukua arvotaan: "))
if montakoLukua < 1:
    print("Virhe!")
else:
    while len(arvottavat) < montakoLukua:
        arvottavaLuku = random.randint(0, 20)
        if arvottavaLuku % 2 != 0:
            continue
        else:
            arvottavat.append(arvottavaLuku)
            if arvottavaLuku > suurinLuku:
                suurinLuku = arvottavaLuku
            if arvottavaLuku < pieninLuku:
                pieninLuku = arvottavaLuku

    print("Suurin:", suurinLuku, "ja pienin:", pieninLuku)

    arvottavat.sort()

    for i in arvottavat:
        if i != arvottavat[len(arvottavat) -1]:
            print(i, end=",")
        else:
            print(i)

#Tässä tulostus häröilee kun useampi arvottava