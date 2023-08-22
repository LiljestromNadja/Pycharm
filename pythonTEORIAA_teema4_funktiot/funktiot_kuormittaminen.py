"""
funktiot - kuormittaminen

- Python EI tue funktioiden kuormittamista (overloading)
- Kuormittamisella tarkoitetaan siis sitä, että samanniminen funktio määritellään useampaan kuin yhteen kertaan ja funktion
parametrit poikkeavat toisistaan. Funktion nimi siis säilyy samana
- Jos funktio on määritelty kahteen kertaan, viimeisin on se jota kääntäjä käyttää
"""

def tulosta_ala(ala):
    print("Ala on", ala)
    return # ei palauta mitään

def tulosta_ala(leveys, korkeus):
    print("Ala on", palauta_ala(leveys, korkeus))
    return #Ei palauta mitään

def palauta_ala(leveys, korkeus):
    ala = leveys * korkeus
    return ala #palauttaa yhden luvun

tulosta_ala(20) #tässä tulee virhe, koska tulosta_ala on määritelty uudelleen
tulosta_ala(23,11)