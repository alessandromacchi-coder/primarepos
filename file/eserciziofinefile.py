dati = open("dati", "w")

while True:
    parola=str(input())

    if parola=="fine":
        print("se hai scritto fine per uscire scrivi y")
        scelta= str(input())
        if scelta == "y":
            break;
    else:
        dati.write(parola + " ")

dati.close()