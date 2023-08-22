"""
teema 2 while
h5
Lue käyttäjältä 7 lukua while -silmukassa (siis yksi luku per kierros). Tulosta lopuksi syötetyistä luvuista pienin ja suurin
"""

laskuri = 1
suurin = -999999999999999 #Laitetaan alkuarvoksi mahdollisimman pieni luku, jottei käyttäjä todennäköiseti anna tällaista lukua
pienin = 99999999999999 # Laitetaan alkuarvoksi mahdollisimman suuri luku, käyttäjä ei todennäköisesti syötä tätä pientä lukua pyydettäessä

while True:
    arvo = int(input("Annapa " + str(laskuri) + ". luku: "))
    if arvo < pienin:
        pienin = arvo
    if arvo > suurin:
        suurin = arvo
    if laskuri >= 7:
        break
    laskuri = laskuri + 1



print("Suurin oli", suurin)
print("Pienin oli", pienin)