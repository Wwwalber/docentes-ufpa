class classeDocente:
    def __init__(self, status):
        self._tipo = "Concurso para docentes"
        self._status = status  # Changed this to accept the status directly

        #self._status = ['N','A','F'] # N: Novo, A: Andamento, F: Finalizado
    
    def __str__(self):
        return f"{self._tipo} - Status: {self._status}"
        
    @property
    def status(self):
        """ retorna o status do tema do concurso """
        status_dict = {'N': 'Novo', 'A': 'Andamento', 'F': 'Finalizado'}
        return status_dict.get(self._status, 'Desconhecido')
    
    def alternar_estado(self, novo_estado):
        """ altera o estado do concurso """
        if novo_estado in ['N', 'A', 'F']:
            self._status = novo_estado
        else:
            print("Estado inválido. Use 'N', 'A', ou 'F'.")

    