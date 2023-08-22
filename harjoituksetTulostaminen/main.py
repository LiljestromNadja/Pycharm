#H1
"""Esittele muuttujat kurssinNimi ja arvosana ja alusta ne jotenkin järkevästi.
Tulosta muuttujien avulla seuraavasti MOLEMMILLA tavoilla (eli käyttäen + tapaa ja {o} tapaa.
"Olet kurssilla ohjelmoinnin perusteet ja sait arvosanan 5" """

kurssinNimi = "Ohjelmoinnin perusteet "
arvosana = 5

#plussatapa
print("Olet kurssilla " + kurssinNimi + " ja sait arvosanan " + str(arvosana)) #muutetaan muuttuja arvosana merkkijonoksi str() -funktiolla

#ns. lokerotapa
print("Olet kursilla {0} ja sait arvosanan {1}".format(kurssinNimi, arvosana)) #määritellään .format() -funktiolla tulostusjärjestys

#Lisäksi pilkkutapa
print("Olet kurssilla", kurssinNimi, "ja sait arvosanan", arvosana )
