#Crea una funzione che prenda in input
#una lista di numeri interi e restituisca la
#somma di tutti i numeri nella lista.

def somma(lista):
    somma=0
    for numero in lista:
        somma+=numero
    return (somma)

listanum = [23, 42]
print(somma(listanum))

#Crea una funzione che prenda in input
#una stringa e restituisca una nuova
#stringa in cui le vocali sono sostituite dal
#carattere "-".

def vocsost(parola):
    vocali= "aeiouAEIOU"
    senzavocali=""
    for lettera in parola:
        if lettera in vocali:
            senzavocali+="-"
        else:
            senzavocali+=lettera
    
    return (senzavocali)

parolatest="ciaocomeva"
print(vocsost(parolatest))

#Crea una funzione che prenda in input due liste di numeri interi e restituisca una nuova
#lista contenente solo gli elementi comuni.


def listacom(lista1, lista2):
        comuni=[]
        for numero in lista1:
            if numero in lista2:
                comuni.append(numero)

        return (comuni)

listacomuni = [23, 43, 55]
print(listacom(listanum, listacomuni))

