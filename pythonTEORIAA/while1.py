"""
While -toistorakenne

- while -toistorakenne(silmukka) on alkuehtoinen toistorakenne, jossa toistoehto testataan ennen kuin suoritetaan yhtään
lausetta rakenteen sisältä.
    - välttämättä ei siis mennä yhtään kertaa silmukan sisälle jos ehto on heti epätosi
    - varsinkin alussa tulee myös helposti ns. ikuisia silmukoita eli ehto pysyy aina totena ja silmukka pyörii ikuisesti

#Jos ehto on tosi, tehdään lauseet ja palataan sitten testaamaan ehto
#Kun ehto tulee epätodeksi, poistutaan luupin(sisennysten) ulkopuolelle

while(ehto)
    tee jotain
    tee jotain muuta

tee täällä jotain luupin jälkeen
"""

#Esimerkki jossa tulostetaan lukuja 0...9 allekkain while-silmukassa

x = 0 #Kierroslaskuri 1
while(x < 10):
    print("Kierros: ", x) #Tässä tulostuu jokaisella kierroksella x, joka kasvaa + 1:llä jokaisella kierroksella
    x = x + 1 #Tässä x:ään lisätään 1 joka kierroksella. tämä jatkuu kunnes ehto x<10 on epätosi.

kierrokset = 0
while(kierrokset < 100):
    print("Kierros: ", kierrokset)
    kierrokset = kierrokset + 1
