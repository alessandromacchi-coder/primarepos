caratteri= open("caratteri","r")
pari= open("pari","w")
dispari=open("dispari","w")

for linea, contenuto in enumerate(caratteri, start=1):
    if linea %2 == 0:
        pari.write(contenuto)
    else:
        dispari.write(contenuto)

pari.close()
dispari.close()
caratteri.close()
