"""
Switch-case
SWITCH-CASE valintarakennetta ei ole Pythonissa, MUTTA

- Switch case rakennehan on tilanteisiin, joissa if-else haaroja on paljon ja koodista meinaa tulla rumaa

- Pythonissa osa tuollaisista tilanteista voidaan ratkaista listalla (directory), jossa on avain-arvo -pareja.
Toimii erityisesti tilanteissa, joissa yhtä avainta vastaa yksi arvo, esim. arvosana 5 on tekstinä kiitettävä eli "5" : "Kiitettävä"
- Toteutetaan siten, että määritellään avain-arvoparit listaan. Sieltä haetaan avaimen perusteella arvo, joten erillistä
if-else -hässäkkää ei tarvita.
"""
#KUUKAUDET
#Luodaan lista, jossa avain-arvo -pareja, HUOMAA kaarisulut ja kaksoispisteet

choices = {"1" : "tammikuu", "2": "helmikuu", "3": "maaliskuu", "4": "huhtikuu",
           "5": "toukokuu", "6": "kesäkuu", "7": "heinäkuu", "8": "Elokuu",
           "9": "syyskuu", "10": "lokakuu", "11": "marraskuu", "12": "joulukuu"}

#Haetaan listasta avainta vastaava arvo
result = choices.get("13", "Unknown")
print(result)
result = choices.get("1", "Unknown")
print(result)

#ARVOSANAT
#Luodaan lista, jossa avain-arvo -pareja, HUOMAA kaarisulut ja kaksoispisteet
choices = {0: "Hylätty", 1: "Tyydyttävä", 2: "Tyydyttävä", 3: "Hyvä", 4: "Hyvä", 5: "Kiitettävä"}
arvosana = int(input("Anna arvosana: "))
result = choices.get(arvosana, "Error")
print("Sait kurssista " + result + " arvosanan.")



"""#ARVOSANAT Tässä kokeilin if-lausetta, toimii, jos käyttäjä ei anna lukua 1-5, konsoliin tulostuu "error"
#Luodaan lista, jossa avain-arvo -pareja, HUOMAA kaarisulut ja kaksoispisteet
choices = {0: "Hylätty", 1: "Tyydyttävä", 2: "Tyydyttävä", 3: "Hyvä", 4: "Hyvä", 5: "Kiitettävä"}
arvosana = int(input("Anna arvosana: "))
if(arvosana == 0 or arvosana == 1 or arvosana == 2 or arvosana == 3 or arvosana == 4 or arvosana == 5):
    result = choices.get(arvosana, "Error")
    print("Sait kurssista " + result + " arvosanan.")
else:
    print("error")"""