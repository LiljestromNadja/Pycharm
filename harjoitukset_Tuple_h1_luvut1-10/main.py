"""
Tuple
h1
Luo tuple jossa on kokonaisluvut väliltä 1-10
Tulosta luvut lopusta alkuun jokainen numero omalle rivilleen

(Tuple siis oli muuten samanlainen kuin lista mutta sen arvoja ei voi muuttaa, ei lisätä tai poistaa luomisen jälkeen)
"""

numerot = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # Tuple luodaan suluilla

for i in range(len(numerot) -1, -1, -1):  # Lähdetään liikkeelle viimeisestä, merkitään -1, mennään ykköseen merkitään -1, siirtymä yhden välein merkitään -1 koska mennään "alaspäin"
    print(numerot[i])

# Toinen tapa
listaksi = list(numerot)
listaksi.reverse()
for luku in listaksi:
    print(luku)



