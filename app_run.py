from modelo.concurso import Concurso

""" criando concursos para teste """
concurso_ufpa1 = Concurso("001-2024", "UFPA")
concurso_ufpa2 = Concurso("002-2024", "UFPA")


def main():
    """ inicio do app """
    print(concurso_ufpa1)
    print(concurso_ufpa2)

if __name__ == '__main__':
    main()