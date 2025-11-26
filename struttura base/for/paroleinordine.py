#mettere in ordine alfabetico un numero n di parole

n=input("inserisci il numero di parole che vuoi inserire")

nparole = input()
k=0
parole = []

for i in range(nparole):
    parole[i] = input("inserisci la parola numero ", k)
    k+=1

for i in range(nparole - 1):
    for j in range(nparole - i - 1):
        if parole[j].lower() > parole[j + 1].lower():
            parole[j], parole[j + 1] = parole[j + 1], parole[j]

