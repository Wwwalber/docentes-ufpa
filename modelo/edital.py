from .classe_docente import classeDocente
class Edital:
    def __init__(self, numero, ano):
        self._numero = numero
        self._ano = ano
        self.unidades = []
        self._classesdocentes = []
    
    def __str__(self):
        return f"Edital: {self._numero} - Ano: {self._ano}"
    
    def adicionar_tipo_de_docentes(self, classe):
        if isinstance(classe, classeDocente):
            self._classesdocentes.append(classe)

    def listar_tipo_de_docentes(self):
        print(f"\nTipos de docentes para o edital {self._numero}:")
        for i, classe in enumerate(self._classesdocentes, start=1):
            print(f"{i}. {classe._tipo}")

    def adicionar_unidade(self, unidade):
        self.unidades.append(unidade)
    
    @property # informa que é somente leitura
    def listar_unidades(self):
        """ retorna a lista de unidades cadastradas """
        print(f'Unidades cadastradas para a {self.demandante}\n')
        for unidade in self.unidades:
            print(unidade)