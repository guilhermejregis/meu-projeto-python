contidd=totH=totM=0
while True:
    idade=int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo=str(input('Sexo [M/F]: ')).strip().upper()
    if idade>=18:
        contidd+=1
    if sexo=='M':
        totH+=1
    if sexo=='F' and idade<20:
        totM+=1
    option= ' '
    while option not in 'SN':
        option=str(input('Quer continuar? [S/N]: ')).strip().upper()
    if option == 'N':
        break
print('Fim de cadastro')
print(f'Você cadastrou {contidd} pessoas maiores de idade.')
print(f'Cadastrou {totH} homens.')
print(f'Cadastrou {totM} mulheres com menos de 20 anos.')
