"""
Virheen hallinta - try except

- Tähän asti meillä ohjelma on "kaatunut" jos esim. merkkijonoa yritetään muuttaa kokonaisluvuksi tilanteessa,
jossa se sisältää muitakin merkkejä kuin numeroita.
- Try -määreellä aloitetaan ns. suojattu lohko
- Jos lohkon sisällä tapahtuu virhe (ns. kaatuminen), niin ohjelman suoritus siirtyy except -lohkoon, jossa virhetilanne
käsitellään. Esim. tulostetaan käyttäjälle ilmoitus virheellisestä syötteestä.
- Try..except -periaate on samanlainen kuin muissakin ohjelmointikielissä.

- Try -lohkon sisään laitetaan koodi, jossa voi tapahtua virhe (ts ohjelman kaatuminen)
- Except -lohkon sisälle siirrytään jos virhe tapahtuu. Virhe käsitellään lohkossa.
- Else - lohko suoritetaan vain, jos try -lohkossa ei tapahtunut virhettä
- Finally lohko suoritetaan lopuksi, tapahtuipa virhe tai ei

"""
#esimerkki

import datetime

#paivays = datetime.datetime(2022, 21, 5) #Tämä kaatuu koska 21 ei kelpaa kuukaudeksi (yyyy, mm, dd)

#nyt ei kaadu vaan tuottaa ilmoituksen
try:
    paivays = datetime.datetime(2022, 21,5)
except:
    print("Päiväys väärin")
    paivays = datetime.datetime(2000, 1, 1)
else:
    print("Päiväys ok.")
finally:
    print(paivays)


