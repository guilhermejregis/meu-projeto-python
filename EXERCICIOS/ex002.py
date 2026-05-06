class Gafanhoto:
    '''
    Essa classe cria um gafanhoto para o nome e uma idade de uma pessoa

    Para criar um gafanhoto utilize
    variavel=Gafanhoto(nome, idade)
    print(variavel.mensagem())

    '''


    def __init__(self, nome ='vazio', idade=0):
        self.nome=nome
        self.idade=idade


    def aniversário(self):
        self.idade += 1


    def __str__(self):
        return f'{self.nome} é GAFANHOTO(A) e tem {self.idade} anos'


g1=Gafanhoto('Maria', 18)
print(g1)