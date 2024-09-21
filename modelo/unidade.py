class Unidade:
    def __init__(self, nome, sigla):
        self.nome = nome.title()
        self.sigla = sigla

    def  __str__(self):
        return f"Unidade: {self.nome} - {self.sigla}"