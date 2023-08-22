"""
teema2
h7
Lue käyttäjältä kaksi kokonaislukua. Jos niiden summa on suurempi tai yhtä suuri kuin 100, tulosta "aika isot luvut"
Laske summa johonkin muuttujaan ennen if-lausetta
"""

luku1 = int(input("Anna eka kokonaisluku:  "))
luku2 = int(input("Anna toka kokonaisluku:  "))

summa = luku1 + luku2

if(summa >= 100):
    print("Aika isot luvut")