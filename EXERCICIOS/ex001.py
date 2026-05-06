class Gafanhoto:
    def __init__(self):
        self.nome=''
        self.idade=0


    def aniversário(self):
        self.idade += 1


    def mensagem(self):
        return f'{self.nome} é GAFANHOTO(A) e tem {self.idade} anos'


g1=Gafanhoto()
g1.nome='Maria'
g1.idade=18
g1.ani
print(g1.mensagem())