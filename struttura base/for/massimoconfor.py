print("inserisci quanti numeri confrontare")
n=int(input())
print ("inserisci il primo da condrontare ")
numero = int(input())

max=numero

for i in range (1, n, 1, 5,):
    print ("prossimo da confrontare")
    numero = int(input())
    if max < numero:    
        max=numero
    
print ("il numero massimo è: ", max)