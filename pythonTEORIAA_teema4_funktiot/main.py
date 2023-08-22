"""
funktiot

if __name__ = '__main__':
print_hi('Heipat sulle!'

Tämä ei ole funktio vaan ns. ilmoitus "alkutiedostosta"

- Python -kielinen ohjelma ei tarvitse monen muun ohjelmointikielen tapaan varsinaisesti funktioita.

- Funktioita on yleensä kuitenkin Python-ohjelmassa, koska ohjelma kannattaa jakaa pienempiin kokonaisuuksiin
toimintakokonaisuuden ja loogisen järjestyksen ymmärtämiseksi.

- Python -ohjelmassa monille koodaajille tuttua main -funktiota kuvaa if-lohko, jossa tarkastetaan, onko kyseessä
main-tiedosto ja siten pääohjelma. Ko lohkon koodi ajetaan vain, jos tuo Python-tiedosto on se josta ohjelma
käynnistetään. Kyseessä siis EI ole täysin sama asia kuin Main-funktio.

- Funktio on rutiini, joka tekee pienen osan kokonaisesta ohjelmasta.
    - Kaikki mitä ohjelmassa tehdään useampaan kertaan kannattaa laittaa funktioon
    - Monesti selkeyden ja luettavuuden vuoksi myös vain yhden kerran suoritettavat tehtävät voidaan laittaa funktioon

Funktiolle voidaan välittää tietoja (parametrejä) ja se voi myös palauttaa arvon/arvoja kutsukohtaansa.

"""

#Yksinkertaien funktio(ei palauta mitään, ei ota yhtään parametria):

#Luodaan funktio
def tulosta_heipat():
    print("Heipat sulle!")

#Kutsutaan funktiota
tulosta_heipat()
