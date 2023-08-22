"""Teema 2 - FOR
h2
Tulosta for -silmukassa luvut 10...1 allekkain."""

for luku in range(10, 0, -1): # range(Alkuarvo, tavoitearvo mihin asti lasketaan +/- 1, vähennys tai lisäys)
    print(luku)


#Omia juttuja...
print("Tässä omaa testailua, luvut sadasta alaspän nollaan 25 välein")
for luku2 in range(100, 0, -25):
    print(luku2)

print("Nollasta sataan 4 välein")
for luku3 in range(0,101, 4):
    print(luku3)

"""Opettajan esimerkki, jossa voidaan myös luoda lista:"""
print("Opettajan esimerkki jossa luodaan lista: ")
luvut = range(10, 0, -1)
for luku4 in luvut:
    print(luku4)