"""
Do-while -tyyppinen toistorakenne
"""
#Pyydetään lämpötiloja ja lopuksi tulostetaan niiden keskiarvo

lampotilasumma = 0 # Muuttuja summan ylläpitoon
laskuri = 0 # Muuttuja laskemaan montako lämpötilaa on syötetty

print("Syötä lämpötiloja. Lukema > 100 päättää syötön")
while True:
    lampotila = float(input("Anna lukema: "))
    if(lampotila > 100):
        break #Luupista poistutaan kun lämpötila on enemmän kuin 100
    laskuri = laskuri + 1
    lampotilasumma = lampotilasumma + lampotila

#Keskiarvoa ei voida tietenkään laskea, jos ei ole yhtään annettua lämpötilaa
if(laskuri > 0):
    print("Keskiarvo oli: {0:4.1f}".format(lampotilasumma/laskuri))
