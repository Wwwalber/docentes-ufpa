from model.docente import Docente

class Assistente(Docente):
    def __init__(self, tema, status):
        super().__init__(tema, status)

    def __str__(self):
        return f"Assistente {self._tema} - Status: {self._status}"