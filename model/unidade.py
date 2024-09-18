class Unidade:
    def __init__(self, nome, sigla):
        self.nome = nome.title()
        self.sigla = sigla

    def  __str__(self):
        return f"Nome: {self.nome} - {self.sigla}"