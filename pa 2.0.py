print('Gerador de PA')
print('-='* 10)
primeiro=int(input('Primeiro termo: '))
razão=int(input('Razão: '))
termo=primeiro
cont=1
while cont<=10:
    print('{}, '.format(termo), end='')
    cont+=1
    termo+=razão
print('Fim', end='')