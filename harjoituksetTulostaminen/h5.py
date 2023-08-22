#h5
"""Esittele muuttujat, joihin voit tallentaa seuraavat tiedot ja alusta muuttujat alkuarvoilla:
- puhelinnumero
- kengän koko

Tulosta sen jälkeen YHDELLÄ print-komennolla:

Sinun puhelinnumerosi on 0447856337 ja kengän kokosi on muuten 43, missä 0447856337 ja 43 tulostuu muuttujista.

 Tulosta kaksi kertaa sama asia eli toisella kerralla + tavalla ja toisella {o}-tavalla."""

puhnro = "0447856337"
kkoko = 43

print("Sinun puhelinnumerosi on " + puhnro + " ja kengän kokosi on muuten " + str(kkoko))
print("Sinun puhelinnumerosi on {0} ja kengän kokosi on muuten {1}".format(puhnro, kkoko))