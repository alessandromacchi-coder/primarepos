"""
Esercizio pratico
Sfida di programmazione
Metti alla prova le tue competenze creando una classe complessa!
1 Parser di pagine web
Creare una classe che abbia le funzioni di parser di pagine web
2 Metodi getter specifici
A richiesta mi dia il numero di ricorrenze delle chiamate di stile, il numero di tag href, ed
il numero di immagini come singoli metodi getter
3 Incapsulamento
Non mi permetta di accedere all'html e non salvi nessun file
"""


class Parser:
    def __init__(self, html):
        self.html=html

    def numero_href(self):
        return 0
    
    def get_immagini(self):
        return 0
    
