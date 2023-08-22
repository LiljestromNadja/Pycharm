koepisteet = []
while True:
    print("Anna koepisteet (0-20), muu päättää syötön", end="")
    pisteet = int(input())
    if (pisteet < 0 or pisteet > 20):
        break
    koepisteet.append(pisteet) #viedään koepisteet listaan

#summataan pisteet keskiarvon laskentaa varten
pistesumma = 0
for p in koepisteet:
    pistesumma += p

koepisteet.sort() #Lajitellaan
#tsekataan että pisteitä on annettu vähintään yksi
if len(koepisteet) > 0:
    print("Alhaisin pistelukema: ", koepisteet[0])
    print("Korkein pistelukema: ", koepisteet[-1])
    print("Keskiarvo oli {0:2.2f}".format(pistesumma/len(koepisteet)))


#Muodostetaan osalistat kunkin arvosanan perusteella, List comprehension
nollat = [x for x in koepisteet if x >= 0 and x <= 9]
ykkoset = [x for x in koepisteet if x >= 10 and x <= 11]
kakkoset= [x for x in koepisteet if x >= 12 and x <= 13]
kolmoset = [x for x in koepisteet if x >= 14 and x <= 15]
neloset = [x for x in koepisteet if x >= 16 and x <= 17]
viitoset = [x for x in koepisteet if x >= 18]

#Tulostetaan arvosanajakaumat listoissa olevien alkioiden määrän perusteella
print("Nollia oli: ", len(nollat))
print("Ykkösiä oli: ", len(ykkoset))
print("Kakkosia oli: ", len(kakkoset))
print("Kolmosia oli: ", len(kolmoset))
print("Nelosia oli: ", len(neloset))
print("Viitosia oli: ", len(viitoset))