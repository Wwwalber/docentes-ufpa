class Concurso:
    """ representa os concursos criados para as diversas unidades  """

    def __init__(self, identificacao, demandante):
        self.identificacao = identificacao
        self.demandante = demandante
        self.descricao = "Concursos para contratação de docentes para a Universidade Federal do Pará"
        self._edital = []

    def __str__(self):
        """ Retorna uma representação string do concurso """
        return f'{self.identificacao} - {self.demandante} - {self.descricao}'

    def adicionar_concurso(self, classe_docente):
        """ Adiciona um novo concurso à lista de concursos """
        if isinstance(classe_docente, Docente):
            self.concursos.append(classe_docente)
            print(f'Concurso para {classe_docente.tipo} adicionado com sucesso!')

    @property
    def exibir_concursos(self):
        f'Lista de concursos:\n'
        for i, tipo in enumerate(self._edital, start=1):
            mensagem = f'{i}. {tipo._tipo} - Status: {tipo.status}'
            print(mensagem)