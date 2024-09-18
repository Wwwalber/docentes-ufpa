class Edital:
    def __init__(self, edital, ano):
        self._edital = edital
        self._ano = ano
    
    def __str__(self):
        return f"Edital: {self._edital} - Ano: {self._ano}"
    