def moedas(num):
    return f'R${num:.2f}'

def aumentar(num):
    num+=1
    return f'R${num:.2f}'



def diminuir(num):
    num-=1
    return f'R${num:.2f}'



def dobro(num):
    num *=2
    return f'R${num:.2f}'



def metade(num):
    num/=2
    return f'R${num:.2f}'


def resumo(num):
    print('-------------------------')
    print('RESUMO DO VALOR')
    print('-------------------------')
    print('Preço analisado:     ', end='')
    print(f'{moedas(num)}', end='')
    print()
    print('Dobro do Preço:      ', end='')
    print(f'{dobro(num)}', end='')
    print()
    print('Metade do preço:     ', end='')
    print(f'{metade(num)}', end='')
    print()
    print('-------------------------')

