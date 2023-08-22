"""
teema 2 ehdollinen operaattori ja vakiot
h1

Kysy käyttäjältä kurssin arviointi (0-10). Jos käyttäjä syötti >8 niin tulosta "hieno juttu"
muuten tulosta "paremmin olis voinut mennä"
Tulosta teksti muuttujasta ja muuttuja on saanut tulostettavan arvon ehdollisessa operaattorissa. Arvo 8 on sijoitettu vakioon
RAJA_ARVO
"""
#Määritellään funktio RAJA_ARVO, joka palauttaa luvun 8
def RAJA_ARVO():
    return 8

arvio = int(input("Arvioi kurssi numerolla 0-10: "))

if(arvio >= RAJA_ARVO()):
    print("Hieno juttu!")
else:
    print("Paremminkin olisi voinut mennä..")

"""
Toinen tapa: 

RAJA_ARVO = 8

arvio = int(input("Arvioi kurssi numerolla 0-10: "))

if(arvio >= RAJA_ARVO): #HUOM, tässä funktion sulut poistettu
    print("Hieno juttu!")
else:
    print("Paremminkin olisi voinut mennä..")"""

""" 
Vielä yksi tapa:

def RAJA_ARVO():
    return 8
arvio = int(input("Arvioi kurssi numerolla 1-10"))
    
vastine = "Hieno juttu" if arvio >= RAJA_ARVO() else "Paremminkin olisi voinut mennä.." """
