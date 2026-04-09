from utilidadesCeV import moedas

num=(int(input('Digite um valor: ')))
print(f'O seu valor foi {num}.')
print(f'Aumentando seu valor fica {moedas.aumentar(num)}')
print(f'Diminuindo seu valor fica {moedas.diminuir(num)}')
print(f'Dobrando seu valor fica {moedas.dobro(num)}')
print(f'A metade do seu valor fica {moedas.metade(num)}')