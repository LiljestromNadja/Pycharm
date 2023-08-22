"""
Tässä esimerkissä kirjoitetaan kysyttyjä opiskelijatietoja tiedostoon ja luetaan ne sieltä ja tulostetaan näytölle
"""

import os
file = "Users/kayttaja/Documents/Temp/pisteet.txt"
wfile = open(file, "wt")
opiskelijat = list()    # Luodaan tyhjä lista
while True:
    nimi = input("Anna nimi (LOPPU = lopetus): ")
    if nimi.upper() == "LOPPU":
        wfile.writelines(opiskelijat)   # Kirjoitetaan lista opiskelijat kerralla tiedostoon
        wfile.close()
        break
    koepisteet = int(input("Anna koepisteet: "))
    tehtavapisteet = int(input("Anna tehtäväpisteet: "))
    # Huomaa että rivinvaihto lopussa
    opiskelijat.append(nimi + " " + str(koepisteet) + " " + str(tehtavapisteet) + "\n")

rfile = open(file)
lines = rfile.readlines()
for opiskelija in lines:
    tiedot = opiskelija.split()
    k = int(tiedot[1])  # Koepisteet
    t = int(tiedot[2])  # Tehtäväpisteet

    print("Nimi:", tiedot[0], "Koepisteet:", tiedot[1], "Tehtäväpisteet:", tiedot[2])
rfile.close()