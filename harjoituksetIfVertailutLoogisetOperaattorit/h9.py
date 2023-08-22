"""
teema2
h9
Lue käyttäjältä desimaaliarvo. Jos arvo oli välillä:
- 1.25-5.76 niin tulosta "osui väliin"
- 12.1-17.96 niin tulosta "osui toiseen väliin
- muussa tapauksessa tulosta "ei sattunut väleihin
"""

syote = float(input("Anna desimaaliluku:  "))

if(syote >= 1.25 and syote <=5.76):
    print("Osui väliin.")
elif(syote >= 12.1 and syote <= 17.96):
    print("Osui toiseen väliin.")
else:
    print("Ei sattunut väleihin.")