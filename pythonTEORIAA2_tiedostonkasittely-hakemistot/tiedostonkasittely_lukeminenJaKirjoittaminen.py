"""Tiedostonkäsittely - lukeminen ja kirjoittaminen

- Tekstitiedostoon kirjoittaminen ja tekstitiedostosta lukeminen onnistuu näppärästi read ja write -funktioiden avulla
- Tässä esimerkit tiedostojen kirjoittamisesta sekä lukemisesta (mac -kone)"""

# Tuodaan os -moduuli
import os
directory = "Users/kayttaja/Documents/Temp"
file = "nimet.txt"
fileWithPath = os.path.join(directory, file)  #Yhdistetään polku ja tiedostonimi

# Ei tarvitse testata olemassaoloa, koska vanha tuhoutuu

wfile = open(fileWithPath, "wt")  # Kirjoitus tiedostoon, tiedosto luodaan
wfile.write("Mari Muikku \n")  # Rivinvaihto loppuun
wfile.write("Mikko Muikku\n")
wfile.close()   # Suljetaan tiedosto

rfile = open(fileWithPath, "rt")
lines = rfile.read()
print(lines)
rfile.close()

wfile = open(fileWithPath, "at")    # Nyt lisätään nimiä tiedostoon
wfile.write("Annti Ahven\n")
wfile.write("Matti Matikka\n")
wfile.close()   # Taas suljetaan

rfile = open(fileWithPath)
lines = rfile.read()
print(lines)
rfile.close()

rfile = open(fileWithPath)
lines = rfile.readlines()   #Nyt luetaan riveittäin. Muodostuu lista
for nimi in lines:
    print(nimi.split()[0])  # Splitataan nimi ja tulostetaan etunimi
rfile.close()



