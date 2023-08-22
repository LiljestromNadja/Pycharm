"""Tiedostonkäsittely, tiedostot
open -funktio

- "r" - Luku - Oletus. Avaa tiedoston lukemista varten. Kaatuu jos tiedosto ei ole olemassa
- "a" - Lisäys - Avaa tiedoston kirjoittamista varten. Vanha data säilyy. Luo tiedoston , jos ei ole olemassa
- "w" - Kirjoitus - Avaa tiedoston kirjoittamista varten. Vanha data tuhoutuu. Luo tiedoston, jos ei ole olemassa
- "x" - Create - Luo tiedoston, kaatuu jos tiedosto on olemassa

Toinen merkki kertoo tiedoston tyypin eli
- t - tekstitiedosto - Oletus
- b - binääritiedosto (ei käsitellä tällä kurssilla)

- Tiedostoon kirjoitettaessa tiedosto ensin luodaan (tai avataan), tehdään toimenpiteet ja sitten suljetaan.
    - jos tiedosto jää auki ja sitä yritetään esimerkiksi poistaa niin ohjelma kaatuu
    - toki myöskin jos käyttäjällä ei ole oikeutta luoda tiedostoa ko hakemistoon niin ohjelma kaatuu"""

#tuodaan os moduuli
import os
directory = "/Users/Kayttaja/Documents/Temp"
file = "nimet.txt"
fileWithPath = os.path.join(directory, file)  #Yhdistetään polku ja tiedostonimi
if (not os.path.exists(fileWithPath)): #Tarkistetaan ensin onko jo olemassa
    # Luodaan tyhjä tiedosto
    open(fileWithPath, "xt")  # x = luodaan, t = tekstitiedosto
    print("Tiedosto", fileWithPath, "luotiin")
else:
    print("Tiedosto", fileWithPath, "on jo olemassa")