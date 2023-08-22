"""
funktiot - rekursio

- python tukee rekursiota eli funktio voi kutsua itseään
- rekursio on erittäin käyttökelpoinen tapa ratkaista tiettyjä matemaattisia ongelmia
- ohjelmoijan täytyy huolehtia (samalla tavalla kuin luupeissa), että sisäkkäiset kutsut joskus päättyvät
- ohessa esimerkki luvun x kertomasta toteutettuna rekursion avulla
"""

def kertoma(x):
    if x == 1:
        return 1
    else:
        return x * kertoma(x-1)

luku = 10
print("Luvun", luku, "kertoma on", kertoma(luku))


print("\nSama käyttäjän syötteellä")
luku2 = int(input("Anna kokonaisluku: "))
print("Luvun", luku2, "kertoma on", kertoma(luku2))