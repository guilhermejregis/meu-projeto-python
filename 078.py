mai=0
men=0
valores=list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    if cont==0:
        mai=men=valores[cont]
    else:
        if valores[cont]>mai:
            mai=valores[cont]
        if valores[cont]<men:
            men=valores[cont]
print(f'O maior valor dos citados é {mai}, e na posição ')
for i, v in enumerate(valores):
    if v==mai:
        print(f'{i}...')
print(f'O menor valor dos citados é {men}, e na posição')
for c, a in enumerate(valores):
    if a==men:
        print(f'{c}...', end='')