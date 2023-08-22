"""
List
h2
Lue käyttäjältä 7 lukua listaan ja tulosta arvot allekkain silmukan avulla
"""

luvut = []

luvut.append(int(input("Anna eka luku: ")))
luvut.append(int(input("Anna toka luku: ")))
luvut.append(int(input("Anna kolmas luku: ")))
luvut.append(int(input("Anna neljäs luku: ")))
luvut.append(int(input("Anna viides luku: ")))
luvut.append(int(input("Anna kuudes luku: ")))
luvut.append(int(input("Anna seitsemäs luku: ")))

for i in luvut:
    print(i)