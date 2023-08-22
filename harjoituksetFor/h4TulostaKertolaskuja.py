"""Teema 2 - FOR
h4
Tulosta for -silmukan avulla seuraavasti:
2 * 9 = 18
3 * 8 = 24
4 * 7 = 28
---
8 * 3 = 24"""

b = 9 # Pienenevä luku

for a in range(2,9):
    print(a, "*", b, "=", (a*b)) # suureneva luku
    b = b -1

"""Toinen tapa """
print("\n\nToinen tapa!!! ")

lista_a = range(2,9)    #Molemmissa listoissa täytyy olla yhtä monta arvoa!!
lista_b = range(9,2,-1)

for a,b in zip(lista_a,lista_b): # zip() -funktio muodostaa listoista avain-arvoparit
    print(a, "*", b, "=", (a*b))