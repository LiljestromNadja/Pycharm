"""
KT2
Luo dictionary, jossa sinulla henkilöiden arvosanoja (0-5). Jos arvosana < 0, niin laitetaan nollaksi ja jos > 5, niin laitetaan viitoseksi. Henkilön nimi on avain ja arvosana arvo. Dictionaryyn ei luonnollisestikaan saa lisätä samannimistä henkilöä uudelleen. Nimiä/arvosanoja kysytään, kunnes nimeksi annetaan LOPPU.

Jos hylättyjä ei ole, niin tulosta kaikkien arvosanojen tiedot (nimi + arvosana). Jos hylättyjä on, niin tulosta hylättyjen määrä näytölle ja sen lisäksi tulosta hylätyn saaneiden henkilöiden nimet.

Toteuta seuraavat funktiot:
LuoNimetJaArvosanat - Kysyy nimet ja arvosanat käyttäjältä ja palauttaa dictionaryn
TulostaHylatyt - Saa parametrina dictionaryn ja tulostaa siitä nollan saaneiden henkilöiden nimet
PalautaHylattyjenMaara - Saa parametrina dictionaryn ja tulostaa siitä nollan saaneiden henkilöiden lukumäärän
TulostaKaikki - Saa parametrina dictionaryn ja tulostaa siitä kaikkien henkilöiden nimet ja arvosanat

Huolehdi, että ohjelma ei kaadu, jos arvosanaksi annetaan muuta kuin numeroita

"""

# Write functions here!

#Kysyy nimen ja arvosanat käyttäjältä ja palauttaa dictionaryn
def LuoNimetJaArvosanat():

    nimetJaArvosanat = dict()

    while True:
        nimi = input("Anna nimi: ").strip()
        if nimi.upper().strip() == "LOPPU":
            break
        if nimi not in nimetJaArvosanat: # Jos nimi ei ole jo dictionaryssa, se lisätään ja kysytään siihen liitettävä arvosana, mutta
            try: #ensin tehdään tämä
                arvosana = int(input("Anna arvosana: ").strip())

            except ValueError: # Jos tulee virhe (eli käyttäjä EI ANNA numeroa), tehdään näin
                print("Arvosanan täytyy olla numero!")
                arvosana = int(input("Anna arvosana: "))

            #ja sitten jatketaan ohjelman suorittamista
            if arvosana < 0:
                arvosana = 0
            if arvosana > 5:
                arvosana = 5

            nimetJaArvosanat[nimi] = arvosana # Liitetään nimeen ja lisätään dictionaryyn

        else:
            print("Opiskelija on jo listassa!")

    return nimetJaArvosanat

# Saa parametrina dictionaryn ja tulostaa siitä nollan saaneiden henkilöiden nimet

def TulostaHylatut(nimetJaArvosanat):
    for i in nimetJaArvosanat:
        if nimetJaArvosanat[i] == 0:
            print(i)

# Saa parametrina dictionaryn ja tulostaa siitä nollan saaneiden henkilöiden lukumäärän

def PalautaHylattyjenMaara(nimetJaArvosanat):
    hylatyt = 0
    for i in nimetJaArvosanat:
        if nimetJaArvosanat[i] == 0:
            hylatyt += 1
    print("Hylättyjä yhteensä:",hylatyt)

# Saa parametrina dictionaryn ja tulostaa siitä kaikkien henkilöiden nimet ja arvosanat

def TulostaKaikki(nimetJaArvosanat):
    for i in nimetJaArvosanat:
        print(i, nimetJaArvosanat[i])

if __name__ == "__main__":
# Write main program below this line

    nimetJaArvosanat = LuoNimetJaArvosanat()
    TulostaHylatut(nimetJaArvosanat)
    PalautaHylattyjenMaara(nimetJaArvosanat)
    TulostaKaikki(nimetJaArvosanat)


