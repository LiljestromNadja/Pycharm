"""
Teema 2 - for
H1

Tulosta for-silmukalla seuraavasti:
1,2,3,4,5,6,7,8,9,10
HUOM! 10 jälkeen ei pilkkua
"""

for luku in range(1, 11):   #luvut 1-10, 11 ei tule mukaan, 1 määritellään sen takia, koska range() funktion alkuarvo on 0
    if luku == 10:          #Tämä on viimeinen luku, jonka jälkeen ei tule pilkkua
        print(luku)
    else:
        print(str(luku) + ", ", end="") # muutetaan luku stringiksi, ja endillä poistetaan rivinvaihto

"""HUOM!!! Pientä ekstraa vakioista!!!"""
"""def MAX():
    return 10

for luku in range(1, MAX() + 1):
    if luku == MAX():
        print(luku)
    else:
        print(str(luku) + ", ", end="")"""