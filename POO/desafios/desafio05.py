from rich.panel import Panel
from rich import print
class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.titulo = nick
        self.favoritos = list()

    def add_favoritos(self, jogo):
        self.favoritos.append(jogo)

    def ficha(self):
        conteudo = f'Nome: [black on blue]{self.nome}[/black on blue]'
        conteudo += f'\nJogos favoritos:'
        for num, jogo in enumerate(self.favoritos):
            conteudo += f'\n[blue]{jogo}[/blue]'
        ficha = Panel(conteudo, title = self.titulo )
        print(ficha)

j1 = Gamer('Guilherme', 'Reginnkk')
j1.add_favoritos('League of Legends')
j1.add_favoritos('Roblox')
j1.add_favoritos('Valorant')
j1.ficha()