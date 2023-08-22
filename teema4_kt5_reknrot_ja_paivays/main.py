"""
import datetime
import os

autot = dict()


def LueAutot():
    while True:
        rekno = input("Anna rekno: ").strip()
        if rekno.upper().strip() == "LOPPU":
            break
        if rekno not in autot:
            luku_onnistui = False
            while not luku_onnistui:
                try:
                    pvmsyote = input("Anna pvm muodossa dd.mm.yyyy: ").strip()
                    pvm = datetime.datetime.strptime(pvmsyote, "%d.%m.%Y")
                    luku_onnistui = True
                except ValueError:
                    print("Väärä muoto! Yritä uudelleen!")


            autot[rekno] = pvm.strftime("%d.%m.%Y")

        else: print("Rekno on jo listassa !!!!")

    for i in autot:
        print(i, autot[i])

LueAutot()"""