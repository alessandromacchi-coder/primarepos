class Studente:
    def __init__(self, nome, cognome, orecrediti, puntiqualita):
        self.nome=nome
        self.cognome=cognome
        self.orecrediti = 0
        self.puntiqualita = 0   

    def calcolagpa(self):
        return self.puntiqualita/self.orecrediti
    
    def stampa(self):
        print(self.nome, "ha un gpa di " , self.calcolagpa())

    def setorecrediti(self, orecrediti):
        self.orecrediti=orecrediti
    
    def setqualita(self, qualita):
        self.qualita=qualita



studente1=Studente("carlo", "maria", 2, 5)

studente1.stampa()
