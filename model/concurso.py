class Concurso:
    """ representa os concursos criados para as diversas unidades  """

    def __init__(self):
        self.descricao = "Concursos para contratação de docentes para a Universidade Federal do Pará"
        self.unidades = []

    def __srt__(self):
        return self.descricao