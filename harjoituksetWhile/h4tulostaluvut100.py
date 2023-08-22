"""
teema 2 while
h4

Laita while-silmukka pyörimään 1-100 yhden välein. Tulosta vain kaikki kolmella (3) jaolliset luvut.
"""

luku = 1

while (luku >= 1) and (luku <= 100):
    luku = luku + 1
    if luku % 3 == 0:
        print(luku)