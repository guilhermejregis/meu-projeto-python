from rich import print
from time import sleep
class Livro:
    def __init__(self, título, pág):
        self.nome = título
        self.pag = pág
        print(f'Você acabou de abrir o livro [blue]{self.nome}[/blue] que possui [yellow]{self.pag} páginas[/yellow].')

    def avancar_paginas(self, qntd):
        self.qntd = qntd
        cont=0
        for c in range(self.qntd):
            if not self.fim():
                print(f' Pág {c+1} ->', end='')
                sleep(0,2)
                cont +=1
        print(f'\nVocê está na página {cont}.')
        if self.fim():
            print('[red]Você chegou no fim do livro[/red]')


    def fim(self)->bool:
        return True if self.qntd == self.qntd else False


c1 = Livro('10 coisas que eu aprendi', 20)
c1.avancar_paginas(21)