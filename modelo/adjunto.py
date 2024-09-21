from model.docente import Docente

class Adjunto(Docente):
    """ Representa um tipo de cargo, uma especialização da classe Docente """
    
    def __init__(self, tema, status):
        super().__init__(tema, status)

    def __str__(self):
        return f"Adjunto: {self.tema}, Status: {self.status}"