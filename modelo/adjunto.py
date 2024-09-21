from modelo.classe_docente import classeDocente

class Adjunto(classeDocente):
    """ Representa um tipo de cargo, uma especialização da classe Docente """
    
    def __init__(self, status):
        super().__init__(status)
        self._tipo = "Concurso para docentes classe Adjunto"
        self._dedicacao = "Dedicação exclusiva"

    def __str__(self):
        return f"{self._tipo}, Status: {self.status}"