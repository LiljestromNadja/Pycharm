"""if-lause"""

luku = 10
merkki = "c"
teksti = "Python-ohjelmointi"
desimaaliluku = 12.56

print("\n\n", luku, merkki, teksti, desimaaliluku, "\n\n")

if(luku > 5):
    print("Kokonaisluku oli suurempi kuin 5")
print("Tämä tulostuu aina, koska ei ole sisennetty edelliseen lohkoon!!!")

if(merkki == "c"):
    print("Tämä tulostuu koska merkki oli oikein eli c")

if(merkki != "a"):
    print("Tämäkin tulostuu koska merkki ei ollut a.")

if(teksti == "Python-ohjelmointi"):
    print("Tulostuu, koska teksti on Python ohjelmointi")

if(desimaaliluku >= 12.55):
    print("Tulostuu, koska desimaaliluku on suurempi kuin 12.55")


if(luku > 0 and luku < 5):
    print("Tulostuu, jos luku on suurempi kuin 0 ja pienempi kuin 5") #Ei tulostu koska molemmat ehdot eivät ole tosia

if(luku > 5 and luku < 15):
    print("Tulostuu, koska luku on suurempi kuin 5 ja pienempi kuin 15")

numero = 2

if(numero == 2):
    print("Numero oli 2")
