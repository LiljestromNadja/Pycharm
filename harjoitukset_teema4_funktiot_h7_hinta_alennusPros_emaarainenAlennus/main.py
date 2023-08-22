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

def maaritaAlePros(osto):
    alennuspros = 0
    if osto < 1000:
        alennuspros = 0
    elif osto >= 1000 and osto < 2000:
        alennuspros = 10
    elif osto >= 2000 and osto < 3000:
        alennuspros = 20
    elif osto >= 3000:
        alennuspros = 30
    return alennuspros

def lasketaysiHinta(osto):
    taysihinta = osto * 10
    return taysihinta

def laskeAleEuroina(taysihinta, alennusprosentti):
    alennusEuroina = taysihinta / 100 * alennusprosentti
    return alennusEuroina

def laskeAlennettuHinta(taysihinta, alennusEuroina):
    alennettuhinta = taysihinta - alennusEuroina
    return alennettuhinta

osto = int(input("Anna kappalemäärä: "))

alennusprosentti = maaritaAlePros(osto)
taysihinta = lasketaysiHinta(osto)
alennusEuroina = laskeAleEuroina(taysihinta, alennusprosentti)
alennettuhinta = laskeAlennettuHinta(taysihinta, alennusEuroina)

print("\nTäysi hinta: {0} euroa\n Alennus euroina: {1} euroa\n Alennus prosenttia: {2} %\n Alennettu hinta: {3} euroa".format(taysihinta, alennusEuroina, alennusprosentti, alennettuhinta))