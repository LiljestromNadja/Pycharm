"""
Teema 4 funktiot osa 2
h7

Tee rekursiivinen funktio, joka laskee summan 1+2+3+....+N, kun N kysytään käyttäjältä pääohjelmassa.
Älä käytä for-luuppia vaan nimen omaan rekursiota.
"""

def summa(n):
    if n == 0:
        return 0
    else:
        return n + summa(n-1)


luku = int(input("Anna luku, jonka summasarja (1+2+3...+N) lasketaan:"))
print(summa(luku))