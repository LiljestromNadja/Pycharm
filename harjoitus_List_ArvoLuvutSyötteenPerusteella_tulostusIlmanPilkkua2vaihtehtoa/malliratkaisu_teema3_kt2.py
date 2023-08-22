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
suurin = -1
pienin = 21
montako = int(input("Montako lukua arvotaan: "))
if montako <= 0:
    print("Virhe!")
else:
    luvut = list()
    while (len(luvut) < montako):
        luku = random.randint(0,20)
        if luku % 2 != 0:
            continue # Ei parillinen
        else:
            luvut.append(luku)
            if luku > suurin:
                suurin = luku
            if luku < pienin:
                pienin = luku
    print("Suurin:", suurin, "ja pienin:", pienin)
    eka  = True
    for luku in luvut:
        if (not eka):
            print(",",end = "")
        eka = False
        print(str(luku),end = "")
    print()