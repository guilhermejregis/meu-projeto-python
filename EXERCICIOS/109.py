from utilidadesCeV import moedas

num=int(input('Digite um valor: '))
print(f'O valor digitado foi {moedas.moedas(num)}')
print(f'Aumentando o valor {moedas.moedas(num)} fica {moedas.aumentar(num)}')
print(f'Diminuindo o valor {moedas.moedas(num)} fica {moedas.diminuir(num)}')
print(f'Dobrando o valor {moedas.moedas(num)} fica {moedas.dobro(num)}')
print(f'A metade do valor {moedas.moedas(num)} fica {moedas.metade(num)}')