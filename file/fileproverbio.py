#utente inserisce un proverbio e io lo scrivo dentro un file, scrivi i caratteri pari in un file "pari" e i dispari in un file "dispari"

import os

proverbio=input("inserisci il proverbio ")
fprov=open("proverbio", "w")
pari=open("pari", "w")
dispari=open("dispari","w")


fprov.write(proverbio)
fprov=open("proverbio", "r")

for i, contenuto in enumerate(fprov.read()):
    if contenuto== " ":
        continue
    if i %2 == 0:
        pari.write(contenuto)
    else:
        dispari.write(contenuto)

pari.close()
dispari.close()
fprov.close()