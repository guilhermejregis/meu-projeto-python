from  rich import print
class Caneta:
    def __init__(self, cor='azul'):
        cor = cor.lower().strip()
        if cor == 'azul':
            escolha = '[blue]'
        elif cor == 'verde':
            escolha = '[green]'
        elif cor == 'vermelho':
            escolha = '[red]'
        else:
            escolha = '[white]'
        self.cor = escolha
        self.tampada = True


    def escrever(self, msg):
        if self.tampada:
            print('A caneta está tampada.')
        else:
            print(f'{self.cor}{msg}[/]', end='')



    def quebrarlinha(self, qntd):
        for c in range(qntd):
            print()


    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False


c1 = Caneta('azul')
c2 = Caneta('vermelho')
c3 = Caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()
c3.escrever('Olá mundo!')
c3.quebrarlinha(0)
c2.escrever('Funciona!')

