class Docente:
    def __init__(self, tema, status):
        self._tema = tema.upper()
        self._status = ['N','A','F'] # N: Novo, A: Andamento, F: Finalizado
        
    @property
    def status(self):
        """ retorna o status do tema do concurso """
        status_atual = ''
        if self._status == 'N':
            status_atual = 'Novo'
        elif self._status == 'A':
            status_atual = 'Andamento'
        elif self._status == 'F':
            status_atual = 'Finalizado'
        return status_atual
    
    def alternar_estado(self, novo_estado):
        """ altera o estado do tema do concurso """
        self._status = novo_estado
    