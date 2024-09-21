class Concurso:
    """ representa os concursos criados para as diversas unidades  """

    def __init__(self, identificacao, demandante):
        self.identificacao = identificacao
        self.demandante = demandante
        self.descricao = "Concursos para contratação de docentes para a Universidade Federal do Pará"

    def __str__(self):
        """ Retorna uma representação string do concurso """
        return f'{self.identificacao} - {self.demandante} - {self.descricao}'

 