"""
teema 4
h5

Tee kysyLuku -funktio, jossa luetaan käyttäjältä int-arvo ja palautetaan se.
Tee laskeSumma -funktio, joka ottaa parametrikseen kaksi int-arvoa ja palauttaa niiden summan.
Tee tulosta -funktio, joka ottaa parametrikseen kolme int-arvoa (eli kaksi lukua ja niiden summan). Eli lue
käyttäjältä kaksi lukua ja tulosta laskutoimitus vastauksineen.
"""

def kysyLuku():
    luku = int(input("Anna luku:"))
    return luku

def laskeSumma(luku1, luku2):
    summa = luku1 + luku2
    return summa

def tulosta(luku1, luku2, summa):
    print("Lukujen {0} ja {1} summa on {2}".format(luku1, luku2, summa))

luku1 = kysyLuku()
luku2 = kysyLuku()

summa = laskeSumma(luku1, luku2)

tulosta(luku1, luku2, summa)
