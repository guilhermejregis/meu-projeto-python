somaidade = 0
maior = 0
nomevelho = ''
média=0
novasmulheres = 0
for c in range(1, 5):
    print('{} Pessoa'.format(c))
    nome=str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo=str(input('Sexo [M/F]:')).strip().upper()
    somaidade += idade
    if sexo in 'F' and idade < 20:
        novasmulheres += 1
    if c == 1 and sexo in 'M':
        maior = idade
        nomevelho = nome
    if sexo in 'M' and idade > maior:
        maior = idade
        nomevelho = nome
média = somaidade /4
print('A média de idade do grupo é igual a {} anos'.format(média))
print('O homem mais velho é {} e ele tem {} anos'.format(nomevelho, maior))
print('Ao todo são {} mulheres com menos de 20 anos'.format(novasmulheres))
