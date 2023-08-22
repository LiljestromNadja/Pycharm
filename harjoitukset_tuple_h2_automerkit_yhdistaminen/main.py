"""
tuple
h2

Luo Tuple, jossa automerkit Volvo, Mersu, Pösö ja Volski. Muodosta sitten uusi tuplem jossa on em tuplen
sisältö lisättynä automerkillä Sitikka. Huomaa että käytät aiempaa tuplea muodostaessasi uutta. Tulosta lopuksi
autot tuplesta.
"""

automerkit = ("Volvo", "Mersu", "Pösö", "Volski") #luodaan tuple

autot = list(automerkit)    #Muutetaan tuple autot -listaksi
autot.append("Sitikka")     #Lisätään listaan sitikka

automerkit = tuple(autot)   #muutetaan autot -lista tupleksi

for auto in automerkit:     
    print(auto)