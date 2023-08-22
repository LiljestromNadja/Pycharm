"""
if-else-if

"""

vastaus = input("Oletkos kotoisin Pohjois-Savosta? kyllä/ei  ")

if(vastaus == "kyllä" or vastaus == "Kyllä"):
    print("Hieno juttu, savolaisuus on parhautta!")
elif(vastaus == "KYLLÄ"):
    print("Elähän kuitenkaan huua!")
elif(vastaus == "ei" or vastaus== "EI" or vastaus == "Ei"):
    print("Ok, kyllähän täällä siedetään muitakin kuin savolaisia")
else:
    print("Tarkistapa vastauksesi kirjoitusasu....")