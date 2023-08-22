#h3
"""Lue käyttäjältä kaksi kokonaislukuarvoa siten, että ensin luet arvon merkkijonona syote -muuttujaan ja sen 
jälkeen konvertoit sen jollakin tapaa muuttujaan luku1. Sama juttu luku2 muuttujan kanssa. 
Tulosta lopuksi lukujen summa näytölle."""

syote = input("Anna ensimmäinen luku: ")
syote2 = input("Anna toinen luku: ")

luku1 = int(syote) #merkkijono muutetaan numeeriseksi arvoksi int() -funktiolla
luku2 = int(syote2)

print("Syöttämiesi lukujen summa on: ",luku1 + luku2)

#TAI
summa = luku1 + luku2
print("Syöttämiesi lukujen summa on ", summa)