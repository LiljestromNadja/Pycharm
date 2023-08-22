"""
while
"""

#tulostetaan parilliset luvut väliltä 0-20

luku = 0
while(luku < 20):
    if(luku % 2 == 0):
        print("Luku: ", luku, "on parillinen")
    luku += 1 #Sama kuin luku = luku + 1

""""
#tulostetaan parittomat luvut väliltä 0-20
while(luku < 20):
    if(luku % 2 != 0): #Jakojäännös EI OLE 0, joten luku on pariton
        print("Luku: ", luku, "ei ole parillinen")
    luku = luku + 1 
    """
#pyydetään lukua niin kauan kunnes käyttäjä antaa luvun väliltä 1...5
luku = 0 #Laitetaan luvuksi nolla, jotta menee edes kerran luuppiin
while(luku < 1 or luku > 5):
    luku = int(input("Anna luku väliltä 1-5: "))
print("Annoit luvun", luku, "ja nyt se on väliltä 1-5")


