"""
If-else if -else - tässä kaksi tapaa toteuttaa sama asia:
    - erilliset IF-lauseet
    TAI
    - yksi if-else if -else rakenne

Kerrotaan onko käyttäjän syöttämä luku on negatiivinen, 0 , tai positiivinen
"""

luku = int(input("Annapa luku:  "))

# Erilliset if-lauseet, toimii, mutta aika tehotonta ja ei niin nättiä

if(luku < 0):
    print("Syöttämäsi luku", luku, "on negatiivinen.")
if(luku == 0):
    print("Luku on nolla.")
if(luku > 0):
    print("Syöttämäsi luku", luku, "on suurempi kuin nolla.")


# Seuraavassa sama yhdellä if-else-if-else lauseella

if(luku < 0):
    print("Syöttämäsi luku", luku, "on negatiivinen")
elif(luku == 0):
    print("Luku on nolla.")
else:
    print("Syöttämäsi luku", luku, "on suurempi kuin nolla. ")