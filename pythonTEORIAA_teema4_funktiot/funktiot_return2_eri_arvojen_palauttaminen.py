"""
Jos funktio esimerkiksi palauttaa eri arvoja eri tilanteissa, niin toki tämä voidaan tehdä laittamalla useampi
return-lause funktioon, mutta parempi tapa on palauttaa arvo vain yhdestä paikasta.
    - Sama asia kuin toistorakenteissa, joissa silmukan pitäisi loppua aina ehtoon (vrt. break) niin
    funktioistakin tulisi palauttaa arvo vain yhdestä paikasta.
"""
#tapa 1
print("Esimerkki 1!")
def laske_arvosana(koepisteet):
    if koepisteet < 10:
        return 0
    elif koepisteet >= 10 and koepisteet <= 12:
        return 1
    elif koepisteet >= 13 and koepisteet <= 14:
        return 2
    elif koepisteet >= 15 and koepisteet <= 16:
        return 3
    elif koepisteet >=17 and koepisteet <= 18:
        return 4
    else:
        return 5

annetutkoepisteet = int(input("Anna koepisteet, lopetus 200: "))

while True:
    if annetutkoepisteet != 200:
        print("Arvosana on: ", laske_arvosana(annetutkoepisteet))
        annetutkoepisteet = int(input("Anna koepisteet:"))
    if annetutkoepisteet == 200:
        print("Lopetit ohjelman")
        break

#tapa 2, opettaja suosittelee
print("Esimerkki 2!")
def laske_arvoSana(koepisteet):
    arvosana = 0
    if koepisteet < 10:
        arvosana = 0
    elif koepisteet >= 10 and koepisteet <= 12:
        arvosana = 1
    elif koepisteet >= 13 and koepisteet <= 14:
        arvosana = 2
    elif koepisteet >= 15 and koepisteet <= 16:
        arvosana = 3
    elif koepisteet >= 17 and koepisteet <= 18:
        arvosana = 4
    else:
        arvosana = 5

    return arvosana

annetutpisteet = int(input("Anna koepisteet, lopetus 200: "))

while True:
    if annetutpisteet != 200:
        print("Arvosana on: ", laske_arvoSana(annetutpisteet))
        annetutpisteet = int(input("Anna koepisteet:"))
    if annetutpisteet == 200:
        print("Lopetit ohjelman")
        break
