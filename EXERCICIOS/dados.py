from utilidadesCeV import moedas
from uteis import cores
def leiaDinheiro(num)
    if num.isnumeric():
        print(f'{moedas.resumo(num)}')
    else:
        print(f'{cores.vemelho(ERRO! Digite um número válido!)}')