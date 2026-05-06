class ContaBancária:
    '''
    Cria uma conta bancária que consegue relizar saques e depósitos.
    '''

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo


    def __str__(self):
        return f'A conta {self.id}, do titular {self.titular}, tem R${self.saldo:.2f} de saldo.'


    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito autorizado de R${valor:.2f}.')


    def saque(self, valor):
        if self.saldo < valor:
            print('Saque negado, seu saldo é menor que seu saque.')
        else:
            print(f'Saque autorizado de R${valor:.2f}.')
            self.saldo -= valor



c1=ContaBancária(112, 'Guilherme', 3000)
c1.deposito(500)
c1.saque(200000000)
print(c1)