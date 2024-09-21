class Edital:
    def __init__(self, numero, ano):
        self._numero = numero
        self._ano = ano
        self.unidades = []
    
    def __str__(self):
        return f"Edital: {self._numero} - Ano: {self._ano}"
    
    def adicionar_unidade(self, unidade):
        self.unidades.append(unidade)
    
    @property # informa que é somente leitura
    def listar_unidades(self):
        """ retorna a lista de unidades cadastradas """
        print(f'Unidades cadastradas para a {self.demandante}\n')
        for unidade in self.unidades:
            print(unidade)