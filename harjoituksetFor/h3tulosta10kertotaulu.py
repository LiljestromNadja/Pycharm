"""Teema 2 - FOR
h3
Tulosta for -silmukalla käyttäjältä kysytyn luvun 10 kertotaulu"""

luku = int(input("Anna kokonaisluku: "))
kertoja = 0

for kertoja in range(1, 11):
    print(luku,  "*", kertoja, "=", luku * kertoja)