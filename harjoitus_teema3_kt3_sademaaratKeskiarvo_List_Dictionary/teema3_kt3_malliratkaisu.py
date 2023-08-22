"""
Teema 3
kt 3
Kysy käyttäjältä ensin kieli (suomi = 0 / Englanti = 1). Oletuskieli on suomi eli muu kuin 0 tai 1 tarkoittaa suomenkielistä
tulostusta. Määrittele koodissa viikonpäivien (ma, ti, ke) tekstit yhteen listaan, jossa on alkio/päivä, eli siis molempien
kielien viikonpäivänimet (esim Maanantai/monday).
Kyse on siis rakenteesta lista listassa.

Ota käyttöön muuttuja (dictionary -tyyppinen), johon voit tallentaa maanantain ja perjantain välisenä aikana neljä mittaustulosta
jokaiselta päivältä. Mittaustulos on sademäärä milleinä. Lue käyttäjältä nämä mittaustulokset ja laske vasta lopuksi ja
tulosta jokaisen päivän mittaustulosten keskiarvo yhdellä desimaalilla seuraavan esimerkin mukaisesti:

Maanantai:      12.0 mm
Tiistai:        0.0 mm
Keskiviikko:    1.9 mm
Torstai:        22.8 mm
Perjantai:      0.9 mm

Esimerkkiajo ohessa:
Millä kielellä /Please choose language (0 = suomi, 1 = english): 1
Monday 1. : 3
Monday 2. : 2
Monday 3. : 4
... Säästetty tilaa...
Friday 2. : 6
Friday 3. : 5
Friday 4. : 3

Monday 3.5 mm
Tuesday 3.2 mm
Wednesday 4.0 mm
Thursday 4.2 mm
Friday 4.8 mm

Syötteiden järkevyydestä ei tarvitse välittää!

Ole taas huolellinen tulostusten kanssa!
"""

paivat  = [["Maanantai","Monday"], ["Tiistai", "Tuesday"], ["Keskiviikko", "Wednesday"], ["Torstai", "Thursday"], ["Perjantai", "Friday"]]
kieli = int(input("Millä kielellä /Please choose language (0 = suomi, 1 = english): "))
if kieli != 1:
    kieli = 0

sademaarat = dict()

for vkpv in paivat:
    paivalukemat = list()
    for i in range(1, 5):
        print(vkpv[kieli], (str(i)+ ". : "), end="")
        sademaara = int(input())
        paivalukemat.append(sademaara)

    sademaarat[paivat.index(vkpv)] = paivalukemat

print()
for paiva in sademaarat:
    print((paivat[paiva])[kieli], end = " ")
    print("{0:.1f} mm".format(sum(sademaarat[paiva])/ len(sademaarat[paiva])))
