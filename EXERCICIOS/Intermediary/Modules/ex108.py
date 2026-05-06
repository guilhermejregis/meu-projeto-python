from utilidadesCeV import moedas

num=(int(input('Digite um valor: ')))
print(f'O seu valor foi {moedas.moeda(num)}.')
print(f'Aumentando o valor {moedas.moeda(num)} fica {moedas.moeda(moedas.aumentar(num))}')
print(f'Diminuindo o valor {moedas.moeda(num)} fica {moedas.moeda(moedas.diminuir(num))}')
print(f'Dobrando o valor {moedas.moeda(num)} fica {moedas.moeda(moedas.dobro(num))}')
print(f'A metade o valor {moedas.moeda(num)} fica {moedas.moeda(moedas.metade(num))}')