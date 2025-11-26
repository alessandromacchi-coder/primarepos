#realizza una rubrica per la gestione dei clienti, piva, nome azienda, città, cap, provincia
#bisogna poter inserire nuovi dati o ricercare un cliente
rubrica={}

while True:
    scelta=int(input("premi 1 per inserire una nuova partita iva o 0 per cercarne una, 2 per stampare tutto il dizio "))
    if scelta==1:
        numeroiva=input()
        dizionario = dict( nomeazienda=str(input("inserisci il nome dell'azienda ")), citta=str(input("inserisci la città ")), cap=int(input("inserici il cap ")))
        rubrica[numeroiva]=dizionario
    elif scelta==0:
        chiave=str(input("dimmi il numero di partita iva"))
        print(rubrica.get(chiave, 0))
    elif scelta==2:
        print(rubrica)