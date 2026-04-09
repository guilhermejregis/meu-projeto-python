from rich import print
from rich.panel import Panel


class Produtos:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def __str__(self):
        return f"{self.nome} custa R${self.preço}"

    def etiqueta(self):
        conteudo= f"{self.nome.center(30)}"
        conteudo += f'{'-'*30}'
        preçof= f'R${self.preço:.2f}'
        conteudo += f'{preçof.center(30, '.')}'
        etiqueta = Panel(conteudo, title='Produto', width=34)
        print(etiqueta)


p1=Produtos('Iphone 17 Pro Max', 25000)
p1.etiqueta()
