from modelo.classe_docente import classeDocente

class Assistente(classeDocente):
    """ Representa um tipo de cargo, uma especialização da classe Docente """
    def __init__(self, status):
        super().__init__(status)
        self._tipo = "Concurso para docente classe Assistente"

    def __str__(self):
        return f"{self._tipo} - Status: {self._status}"