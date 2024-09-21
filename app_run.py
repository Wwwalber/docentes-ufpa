from modelo.edital import Edital
from modelo.assistente import Assistente
from modelo.adjunto import Adjunto

edital1 = Edital('100', 2023)
edital2 = Edital('105', 2023)
edital3 = Edital('129', 2024)

assistente1 = Assistente('A')  # 'A' for 'Andamento'
assistente2 = Assistente('N')  # 'N' for 'Novo'
adjunto1 = Adjunto('F')  # 'F' for 'Finalizado'
adjunto2 = Adjunto('E')  # 'E' for 'Em andamento'
assistente3 = Assistente('F')
adjunto3 = Adjunto('E')
adjunto4 = Adjunto('A')  # 'A' for 'Aguardando'
adjunto5 = Adjunto('C')  # 'C' for 'Cancelado'
adjunto6 = Adjunto('R')  # 'R' for 'Reaberto'
adjunto7 = Adjunto('P')  # 'P' for 'Pendente'
adjunto8 = Adjunto('D')  # 'D' for 'Desistiu'
adjunto9 = Adjunto('T')  # 'T' for 'Transferido'


edital3.listar_tipo_de_docentes()
def main():
    """ inicio do app """
    print(edital1)
    print(edital2)
    print(edital3)

    edital1.adicionar_tipo_de_docentes(assistente1)
    edital1.adicionar_tipo_de_docentes(assistente2)
    edital2.adicionar_tipo_de_docentes(adjunto1)
    edital2.adicionar_tipo_de_docentes(adjunto2)
    edital3.adicionar_tipo_de_docentes(assistente3)
    edital3.adicionar_tipo_de_docentes(adjunto3)
    edital3.adicionar_tipo_de_docentes(adjunto4)
    edital3.adicionar_tipo_de_docentes(adjunto5)
    edital3.adicionar_tipo_de_docentes(adjunto6)
    edital3.adicionar_tipo_de_docentes(adjunto7)
    edital3.adicionar_tipo_de_docentes(adjunto8)
    edital3.adicionar_tipo_de_docentes(adjunto9)

    edital1.listar_tipo_de_docentes()
    edital2.listar_tipo_de_docentes()
    edital3.listar_tipo_de_docentes()

if __name__ == '__main__':
    main()