"""
Funktiot - parametri

- Kun funktiolle välitetään tietoja, puhutaan parametreista
- Parametri on kopio kutsuvan ohjelman funktiole välittämän lausekkeen arvosta
- Lähetetty arvo kopioituu funktion paikalliseen muuttujaan, joka on esitelty parametrilistassa
    - JOS FUNKTION PAIKALLISEN PARAMETRIMUUTTUJAN ARVOA MUUTTAA, niin kutsukohdan muuttujan arvo ei muutu
"""

def laske_tulo(luku1, luku2):
    tulo = luku1 * luku2 # laskee tulon paikalliseen muuttujaan
    return tulo

def tuplaa(luku):
    luku *= 2 #tuplaa parametrimuuttujan
    return luku

tulo = laske_tulo(2, 3)
print(tulo)

luku = int(input("Anna luku"))
tuplattu = tuplaa(luku)
print(tuplattu)

#tai näin
tokaluku = int(input("Anna toinen luku"))
print(tuplaa(tokaluku))



#EI näin!!!
tulo = 0
laske_tulo(2,3)
print(tulo) #Tulostuu 0

luku = 1
tuplaa(luku)
print(luku) #Tulostuu 1





