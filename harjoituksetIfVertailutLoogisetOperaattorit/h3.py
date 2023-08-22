"""
teema 2
h3
Lue käyttäjältä arvosana väliltä 4-10. Jos käyttäjä syötti arvosanan oikein, esim. 5 niin tulosta "Arvosana oli 5"
Muussa tapauksessa tulosta, että "Arvosanan tuli olla väliltä 4-10.
"""

arvosana = int(input("Anna arvosana väliltä 4-10 "))

if(arvosana >= 4 and arvosana <= 10):
    print("Arvosana oli: ", arvosana)
else:
    print("Arvosanan tuli olla väliltä 4-10")