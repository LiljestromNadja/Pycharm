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

    print("Suurin:", max(arvottavat), "ja pienin:", min(arvottavat))

    for i in arvottavat:
        if i != arvottavat[len(arvottavat)-1]:  #Jos i ei ole listan arvottavat viimeinen
            print(i, end=",")
        elif i == arvottavat[len(arvottavat)-1]: #muuten jos i on listan arvottavat viimeinen
            print(i)


    print("Viimeinen", arvottavat[len(arvottavat) - 1])




