"""
List
h5
Kysy käyttäjältä päiväkohtaisia lämpötiloja. Lämpötila <-999 lopettaa arvojen syötön.
Vie lämpötilat listaan.
Käy listan alkiot läpi ja tulosta lopuksi
- kuinka monta lämpötilaa annettiin
- mikä oli niiden keskiarvo
- montako oli hellepäiviä (ltila >=25)
- korkein lämpötila
- pienin lämpötila.

Huolehdi tulostuksessa desimaalilukujen muotoilusta
"""

lampotilat = []
# tai lampotilat = list()

while True:
    ltila = float(input("Anna lämpötila (< -999 lopettaa syötön): "))
    if ltila < -999:
        break
    lampotilat.append(ltila)

# Lajittelu
lampotilat.sort()

print("Lämpötiloja annettiin", len(lampotilat), "kpl")

if len(lampotilat) > 0:
    print("Lämpötilojen keskiarvo oli: {0:2.2f}".format(sum(lampotilat)/len(lampotilat)))
    print("Korkein lämpötila oli:", lampotilat[len(lampotilat)-1])
    print("Alin lämpötila oli", lampotilat[0])

hellepaivat = [x for x in lampotilat if x >= 25]
print("Hellepäiviä oli", len(hellepaivat), "kpl")
