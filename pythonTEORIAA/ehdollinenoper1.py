"""
Ehdollinen operaattori

Ehdollista operaattoria käytetään seuraavasti:

    x = a if True else b

    Tämä on itse asiassa sama kuin if else -lause
"""

ekaluku = int(input("Anna eka luku: "))
tokaluku = int(input("Anna toka luku: "))

#Muuttujaan nimeltä pienempi otetaan talteen kahdesta luvusta pienempi
#Käytetään ehdollista operaattoria

pienempi = ekaluku if (ekaluku < tokaluku) else tokaluku # Eli siis pienempi on ekaluku jos se on pienempi kuin tokaluku, muussa tapauksessa pienempi on tokaluku
print("Pienempi syötetyistä arvoista oli: ", pienempi)

#Tässä sama perinteisellä if-lauseella

if(ekaluku < tokaluku):
    pienempi = ekaluku
else:
    pienempi = tokaluku
print("Pienempi syötetyistä arvoista oli: ", pienempi)