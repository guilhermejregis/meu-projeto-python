from rich import print
from rich import inspect
class Funcionarios:
    def __init__(self, nome, idade, cargo):
        self.nome=nome
        self.idade=idade
        self.cargo=cargo

    def apresentação(self):
        return f'Olá sou [blue]{self.nome}[/blue], tenho {self.idade} anos e sou {self.cargo} da empresa.'


c1= Funcionarios('Maria', 23, 'Programadora')
print(c1.apresentação())
#inspect(c1)

