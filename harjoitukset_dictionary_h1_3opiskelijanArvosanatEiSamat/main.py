"""
Dictionary
h1
Lue käyttäjältä kolmen opiskelijan arvosanat. Opiskelijasta syötetään siis opiskelijanumero ja arvosana 0-5.
Käytä dictionaryä eli huolehdi sen avulla että sama opiskelija (eli siis sama opiskelijanumero) ei ole listoilla
kahteen kertaan. Tulosta lopuksi tiedot
"""


opiskelijat = dict()

while len(opiskelijat) < 3:
    opiskelijanumero = input("Anna opiskelijanumero:")
    if opiskelijanumero not in opiskelijat:
        arvosana = int(input("Anna arvosana 0-5: "))
        opiskelijat[opiskelijanumero] = arvosana
    else:
        print("Opiskelijalla on jo arvosana")

for opiskelija in opiskelijat:
    print(opiskelija, opiskelijat[opiskelija])