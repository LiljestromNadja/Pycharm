"""Teema 2 - FOR
h7
Lue käyttäjältä kuusi arvoa väliltä 1-5 for-silmukassa. Jos käyttäjä ei antanut lukua oikein niin arvo on kysyttävä uudestaan.
Kaatumista ei vielä tarvitse hanskata. Tulosta lopuksi lukujen tulo näytölle. """

for laskuri in range(1,7):
    while True:
        arvo = int(input("Anna luku nro " + str(laskuri) + ": "))
        if (arvo >= 1) and (arvo <=5):
            tulo = arvo * arvo
            break

print(tulo)