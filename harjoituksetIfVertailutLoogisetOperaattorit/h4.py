"""
teema 2
h4
Kysy käyttäjältä onko ohjelmointi kivaa. Jos käyttäjä vastasi kyllä tai KYLLÄ niin tulosta "hyvä juttu"
Muuten tulosta "ei niin hyvä juttu"
"""

vastaus = input("Onko ohjelmointi kivaa? kyllä/ei  ")

if(vastaus == "kyllä" or vastaus == "KYLLÄ"):
    print("Hyvä juttu!")
else:
    print("Ei niin hyvä juttu...")

""" Muista että näissä tilanteissa voi käyttää .upper() -funktiota
esim. 
vastaus = input("onko ohjelmointi kivaa?")
vastaus = vastaus.upper()
"""
