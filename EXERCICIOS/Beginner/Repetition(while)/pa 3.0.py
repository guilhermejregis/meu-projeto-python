print('Gerador de PA')
print('-='* 10)
primeiro=int(input('Primeiro termo: '))
razão=int(input('Razão: '))
termo=primeiro
cont=1
adc=10
total = 0
while adc != 0:
    total+=adc
    while cont<=total:
        print('{}, '.format(termo), end='')
        cont+=1
        termo+=razão
    adc=int(input('Quantos termos quer mostrar mais?'))



