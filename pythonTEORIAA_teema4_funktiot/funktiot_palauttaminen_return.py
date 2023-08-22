"""
Funktiot - palauttaminen(return)
- Tyypillisesti funktiossa on yksi tai useampia return-lauseita
- Return ei ole pakollinen
- Jos funktio ei palauta mitään kutsuvaan osaan, pelkkä return riittää
- Paluuarvo voi olla yksittäinen arvo (kokonaisluku, merkkijono, jne) tai mikä tahansa lista-tyyppinen muuttuja
- Jos funktion pitää palauttaa yksi tai useampi arvo, ne laitetaan listaan ja palautetaan lista
"""

def tulosta_ala(ala):
    print("Ala on", ala)
    return #Ei palauta mitään

def palauta_ala(leveys, korkeus):
    ala = leveys * korkeus
    return ala #palauttaa yhden luvun

def palauta_alat(mitat): #mitat listassa
    alat = list()
    for mitta in mitat:
        ala = mitta[0] * mitta[1]
        alat.append(ala)
    return alat #palautetaan lista jossa alat

palauta_ala(2,3) #Paluuarvoa ei oteta talteen eli se menetetään
ala = palauta_ala(10, 12)
tulosta_ala(ala) # Ei palauta mitään joten paluuarvoa ei voi/tarvitse ottaa talteen

mitat = [[12, 14], [4, 6], [1, 2]]
alat = palauta_alat(mitat)
for ala in alat:
    print(ala)
