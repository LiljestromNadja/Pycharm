"""
teema 4 funktiot osa 2
h4

Arvo listaan 10 lukua väliltä x-y ja tulosta alkiot pilkulla eroteltuna.
Käytä funktioita
kysyXjaY
ArvoLuvut
TulostaLuvut
"""

import random

def kysyXjaY():
    x = int(input("Anna lukujen alaraja: "))
    y = int(input("Anna lukujen yläraja: "))

    return [x, y]

def arvoLuvut(x, y):
    luvut = []

    for i in range(0, 10):
        luku = random.randint(x, y)
        luvut.append(luku)

    return luvut

def tulosta_luvut(luvut):
    for i in range(0, len(luvut)):
        if i == len(luvut)-1: #Huolehditaan ettei rivin loppuun tule pilkkua
            print(luvut[i])
        else:
            print(luvut[i], end=",")

x_ja_y = kysyXjaY()
luvut = arvoLuvut(x_ja_y[0], x_ja_y[1])
tulosta_luvut(luvut)