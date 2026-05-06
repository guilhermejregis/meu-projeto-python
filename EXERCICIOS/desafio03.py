from rich import print
from rich.panel import Panel
class Churrasco:
    def __init__(self, título, qntd):
        self.titulo = título
        self.qntd = qntd


    def analisar(self):
        self.carne = self.qntd * 400
        self.custo = (self.carne / 1000) * 82.40
        self.entrada = self.custo / self.qntd
        conteudo = f'Analisando o [green]{self.titulo}[/green] com [blue]{self.qntd} convidados[/blue]'
        conteudo += '\nCada participante comerá o.4Kg e cada Kg custa R$ 82.40'
        conteudo += f'\nRecomendo [blue]comprar {self.carne}g[/blue] de carne.'
        conteudo += f'\nO custo total será de [green]R${self.custo:.2f}[/green].'
        conteudo += f'\nCada pessoa pagará [yellow]R${self.entrada:.2f}[/yellow] para participar'
        analise = Panel(conteudo, title = f'{self.titulo}', width = 60)
        print(analise)

c1 = Churrasco('Churrasco dos amigos', 15)
c1.analisar()
