divisore = float(input("inserisci il divisore"))
dividendo = float(input("inserisci il dividendo"))

i=0 

while divisore<=dividendo:
    dividendo-=divisore
    i+=1
print("il risultato è ", i )