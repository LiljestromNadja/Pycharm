def kysyJaLaske():
    luku1 = int(input("Anna ensimmäinen luku: "))
    luku2 = int(input("Anna toinen luku: "))
    osam = luku1 / luku2
    return osam

osam = kysyJaLaske()
print("Osamäärä on", osam)