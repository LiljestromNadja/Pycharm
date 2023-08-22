"""Dictionary {}, esimerkki tilaukset"""

tilaukset = {}

while True:
    tilausnumero = int(input("Anna tilausnumero, 0 päättää ohjelman: "))
    if tilausnumero <= 0:
        break
    if tilausnumero in tilaukset:
        print("Tilausnumero on jo syötetty")
        continue
    tuote = input("Anna tuote: ")
    maara = int(input("Anna määrä: "))
    ostotiedot = [tuote, maara]
    tilaukset[tilausnumero] = ostotiedot  # Viedään arvoksi lista, avain on tilausnumero ja arvo ostotiedot -lista avain-arvopareissa

for tilaus in tilaukset:
    print(tilaus, tilaukset[tilaus][0], tilaukset[tilaus][1])
    #Eli print tilausnumero(avain), tuote, määrä