from rich.panel import Panel
from rich import print
class ControleRemoto:
    canal_min :int=1
    canal_max :int=6
    vol_min :int=1
    vol_max :int=6

    def __init__(self, canal = 1, volume = 2):
        self.canal_atual = canal
        self.volume_atual = volume
        self.ligada = False

    def liga_desliga(self):
        self.ligada = not self.ligada

    def iniciar(self):
        if self.ligada==True:
            conteudo = 'CANAL  mín '
            for c in range(ControleRemoto.canal_min, ControleRemoto.canal_max+1):
                if c == self.canal_atual:
                    conteudo += f'[black on yellow] {c} [/] '
                else:
                    conteudo += f' {c} '
            conteudo += 'máx'
            conteudo += '\nVOLUME mín '
            for c in range(ControleRemoto.vol_min, ControleRemoto.vol_max+1):
                if c == self.volume_atual or c < self.volume_atual:
                    conteudo += '[white on white]   [/]'
                else:
                    conteudo += '[black on black]   [/]'
            conteudo += ' máx'



            ligada = Panel(conteudo.center(32), title='TV', width=40)
            print(ligada)
        if not self.ligada:
                desligada = Panel('[red]A TV está desligada[/]'.center(39), title='TV', width=34)
                print(desligada)

    def canal_mais(self):
        if self.ligada:
            if self.canal_atual == self.canal_max:
                self.canal_atual = self.canal_min
            else:
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligada:
            if self.canal_atual == self.canal_min:
                self.canal_atual = self.canal_max
            else:
                self.canal_atual -= 1


    def vol_mais(self):
        if self.ligada:
            if self.volume_atual == self.vol_max:
                self.volume_atual = self.vol_min
            else:
                self.volume_atual += 1


    def vol_menos(self):
        if self.ligada:
            if self.volume_atual == self.vol_min:
                self.volume_atual = self.vol_max



c1=ControleRemoto()
while True:
    cmd = str(input(f'\n  < CH >    - VOL + '))
    if cmd == '0':
        break
    elif cmd == '@':
        c1.liga_desliga()
        c1.iniciar()
    elif cmd == '<':
        c1.canal_menos()
    elif cmd == '>':
        c1.canal_mais()
    elif cmd == '-':
        c1.vol_menos()
    elif cmd == '+':
        c1.canal_mais()
print('\n'*10)