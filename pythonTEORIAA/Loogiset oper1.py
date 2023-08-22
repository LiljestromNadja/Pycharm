"""
Loogiset operaattorit

"""
luku = 1

if(luku >= 5 and luku <= 10):
    print("Luku on suurempi tai yhtä suuri kuin 5 JA pienempi tai yhtä suuri kuin 10.")
    #Koska luku on 1, ei tulostu
if(not(luku >= 5)):
    print("Luku ei ole suurempi tai yhtä suuri kuin 5.")
    #Tulostuu, koska luku 1 ei ole suurempi tai yhtä suuri kuin 5.
if(luku < 5):
    print("Luku on pienempi kuin 5.")
    #Tulostuu, koska luku 1 on pienempi kuin 5.
if(luku < 1 or luku >30):
    print("Luku on pienempi kuin 1 TAI suurempi kuin 30.") #OR ehtolause pitää paikkansa jos jompi kumpi ehdoista toteutuu"
    #Ei tulostu, koska luku 1 ei ole pienempi kuin 1 tai suurempi kuin 30.
    #Tulostuisi jos ehdoissa olisi määritelty (luku <= 1 or luku > 30), koska 1 on yhtä suuri kuin 1

merkki = "e"

if(merkki == "a" or merkki == "A" or merkki == "c"): #Tässä koko ehto on tosi jos joku ehdoista on tosi
    print("Merkki oli e")
    #ei tulostu, koska e ei ole mikään ehdon merkeistä




