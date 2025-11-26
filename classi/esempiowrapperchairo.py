def controlla_admin(funzione):
    def wrapper(utente):
        if utente != "admin":
            print("Accesso negato")
            return
        return funzione(utente)
    return wrapper

@controlla_admin
def pannello_admin(utente):
    print("Benvenuto,", utente)


import time

def timer(funzione):
    def wrapper():
        start = time.time()
        funzione()
        end = time.time()
        print("Tempo:", end - start, "secondi")
    return wrapper

@timer
def lavoro_pesante():
    for _ in range(10_000_000):
        pass
