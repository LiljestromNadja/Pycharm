"""
Teema 4 funktiot osa 2
h 1

Toteuta funktio, joka saa parametrinaan kokonaislukuja (ei rajaa) ja palauttaa niistä suurimman.
"""

def palauta_suurin(*args):
    suurin = float('-inf') #laitetaan alustavasti suurimmaksi tosi pieni luku
    #suurin = -999999 # kävisi näinkin
    for luku in args:
        if luku > suurin:
            suurin = luku
    return suurin

suurin = palauta_suurin(2,4,5,1)
print(suurin)