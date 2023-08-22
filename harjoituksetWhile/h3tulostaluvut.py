"""
teema 2 while
h3

Tulosta luvut -3...9 kolmen välein pilkulla erotettuna samalle riville
"""

# Luodaan muuttuja ja annetaan sille alkuarvo
luku = -3

while luku <= 9:
    if(luku == 9):
        print(luku)
    else:
        print(str(luku) + ",", end=" ") #muutetaan luku stringiksi
    luku = luku + 3

"""TÄSSÄ voi käyttää myös der MAX() -funktiota"""