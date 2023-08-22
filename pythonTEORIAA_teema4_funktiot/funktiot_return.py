"""
funktiot - return

- return-lause kirjoitetaan sellaiseen funktioon joka palauttaa arvon. Pelkkä return ilman palautettavaa arvoa
kirjoitetaan silloin, kun halutaan hypätä funktiosta pois palauttamatta mitään. Funktion palauttamaa arvoa ei ole
pakko käsitellä kutsuvassa osassa ohjelmaa. Silloin palautuva arvo vain "häviää".
"""

#Tämä funktio ei palauta mitään

def tulosta_ala(ala):
    print("Ala on {0:.2f}".format(ala))

#Yksi parametri ja palautusarvo
def kysy_sade():
    vastaus = float(input("Anna säde: "))
    return vastaus

def kysy_valinta():
    valinta = int(input("Anna valinta (1/2/3/4): "))
    if valinta < 1 or valinta > 4:
        return #Tullaan funktiosta pois palauttamatta mitään
    else:
        return valinta

kysy_sade() #Kysytään säde mutta paluuarvoa ei oteta talteen
sade = kysy_sade() #Kysytään säde ja otetaan paluuarvo talteen sade-muuttujaan
tulosta_ala(sade) # Annetaan sade parametrina tulosta_ala funktiolle
valinta = kysy_valinta()
print(valinta) #tulostuu none, jos ei oikea valinta eli tässä tapauksessa 1/2/3/4

