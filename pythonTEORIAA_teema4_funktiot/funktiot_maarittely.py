"""
Funktiot - määrittely

- Funktion määrittely alkaa sanalla def
- Funktiolle on annettava nimi. Nimeämissäännöt samat kuin muuttujilla.
- Nimen jälkeen sulkeisiin laitetaan funktiolle välitettävät parametrit. Jos parametrejä ei ole, sulut ovat kuitenkin
pakolliset.
- Funktion sisään tuleva koodi sisennetään

Tässä esimerkkejä funktioista ja niiden kutsusta
"""

def tulosta_hello():
    print("Hello, hello!")

tulosta_hello()

#tyhjä funktio
def tulosta_heheei():
    pass

#Funktio jolle annetaan parametrina kaksi lukua ja se laskee niiden summan

def tulosta_summa(luku1, luku2):
    print("Lukujen summa oli:", (luku1+luku2))

tulosta_summa(3,4)

#funktio joka kysyy nimen ja palauttaa sen

def kysy_nimi():
    nimi = input("Anna nimi")
    return nimi

nimi = kysy_nimi()
print("Annoit nimen", nimi)

def kysy_jalaske():
    nro1 = int(input("Anna luku: "))
    nro2 = int(input("Anna toinen luku"))
    print("Antamiesi lukujen summa on ", nro1 + nro2)

kysy_jalaske()
