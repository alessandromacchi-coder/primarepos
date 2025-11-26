"""
realizzare sistema di gestione di task

si deve poter:
salvare una lista di attività su un file di testo
leggere le attività dal file una alla volta usando un generatore
gestire eventuali errori che possono verificarsi durante la lettura o scrittura del file

attivita: cosa da fare, contesto, durata (num), data
"""

from datetime import date 
import ast 


memoriatask=open("attività", "w")
leattivita={}

def leggidict(nomefile):
    nomefile=open(nomefile, "r")
    yield nomefile.readline()

"""
def aggiungifile(nomefile, dict):
    try:
        nomefile.write(str(dict) + "\n")
    except:
        print("assicurati di aver inserito i parametri nella maniera corretta e riprova ")
        """
    
while True:
    scelta=input("premi: 1 per aggiungere un'attività, 2 per leggere tutte le attività, 3 per eliminare tutte le task, 4 per leggerle una alla volta ")
    match scelta:
        case "1":
            print("hai scelto di inserire un'attività")
            memoriatask=open("attività", "a")
            task=input("inserisci il nome dell'attività ")
            leattivita[task]=dict(dafare= str(input("inserisci cosa devi fare ")),  contesto=str(input("inserisci il contesto ")), durata=str(input("inserisci la durata dell'attività (in ore) ")))
            memoriatask.write(str(leattivita) + "\n")
            memoriatask.close()
        case "2":
            print("hai scelto di leggere le attività \n")
            memoriatask=open("attività", "r")
            try:
                dizstampa = ast.literal_eval(memoriatask.read()) 
                print(dizstampa)
            except:
                print("database vuoto, inserisci almeno un'attività ")
                continue
            memoriatask.close()
        case "3":
            memoriatask=open("attività", "w")
            leattivita.clear()
            memoriatask.close()
        case "4":
            leggidict(leattivita)
        case "5": 
            break

memoriatask.close()
