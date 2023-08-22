import os


file = "nimet.txt"

wfile = open(file, "wt")
wfile.write("Mari Muikku\n")
wfile.write("Mikko Muikku\n")
wfile.close()

rfile = open(file, "rt")
lines = rfile.read()
print(lines)
rfile.close()

wfile = open(file, "at")
wfile.write("Piippolan vaarilla\n")
wfile.write("Oli talo\n")
wfile.write("Hiialahei heihei")
wfile.close()

rfile = open(file)
lines = rfile.read()
print(lines)
rfile.close()

rfile = open(file)
lines = rfile.readlines()
rivinro = 0
for eka in lines:
    rivinro += 1
    print("{0}. rivi".format(rivinro), "eka: ", eka.split()[0], "toka: ", eka.split()[1])
rfile.close()