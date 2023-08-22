"""
if-else-if
"""

arvosana = int(input("Anna kurssille arvosana väliltä 1-5  "))

if(arvosana == 1):
    print("Ei tainnut oikein mennä putkeen")
elif(arvosana == 2):
    print("No, parannettavaa jäi...")
elif(arvosana == 3):
    print("Keskitasoa.")
elif(arvosana == 4):
    print("Ihan vähän hienosäätöä vielä!")
elif(arvosana == 5):
    print("Loistavaa!")
else:
    print("Et antanut numeroa väliltä 1-5")


