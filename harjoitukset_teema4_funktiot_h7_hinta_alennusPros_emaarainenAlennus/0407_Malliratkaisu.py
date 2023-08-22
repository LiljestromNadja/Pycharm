"""
teema 4
h7

Kirjoita ohjelma joka ilmoittaa tavaraerän hinnan (alennus on otettu huomioon), alennusprosentin ja euromääräisen
alennuksen, kun yksikköhintana on 10 € ja määräalennukset 10%,20% ja 30% saadaan vastaavasti yli 1000:n, 2000:n ja 3000:n
kappaleen eristä. Alussa ohjelma kysyy kuinka monta kappaletta ko tuotetta ostettiin

yksikköhinta - 10 e
ale
osto < 1000 kpl - ei alea
osto >= 1000 kpl - 10%
osto >= 2000 kpl - 20%
osto >= 3000 kpl - 30%

alennettu hinta
alennusprosentti
euromääräinen alennus
"""

def laske_alepros(kpl):
    if kpl > 3000:
        alepros = 30
    elif kpl > 2000:
        alepros = 20
    elif kpl > 1000:
        alepros = 10
    else:
        alepros = 0
    return alepros

def laske_alennus(yksikkohinta, alepros):
    return (yksikkohinta * alepros) / 100

def laske_hinta(kpl, yksikkohinta):
    alepros = laske_alepros(kpl)
    alennus = laske_alennus(yksikkohinta, alepros)
    alennettuhinta = yksikkohinta - alennus
    tiedot = list()
    tiedot.append(alennettuhinta)
    tiedot.append(alennus)
    tiedot.append(alepros)
    return tiedot

yksikkohinta = 10
kpl = int(input("Kuinka monta kpl ostettiin: "))
tiedot = laske_hinta(kpl, yksikkohinta)
print("Erän hinta on:", tiedot[0] * kpl)
print("Erän alennus on:", tiedot[1] * kpl)
print("Erän alennus% on:", tiedot[2])