lista=[]
dic={}
soma=média=0
listafem=[]
maioridade=[]
while True:
    dic['Nome: ']=str(input('Nome: ')).upper()
    dic['Idade: ']=int(input('Idade: '))
    soma+=dic['Idade: ']
    if dic['Idade: ']>média:
        maioridade.append(dic.copy())
    dic['Sexo: ']=str(input('Sexo: ')).upper()
    if dic['Sexo: '] in 'F':
        listafem.append(dic.copy())
    lista.append(dic.copy())
    dic.clear()
    resp=str(input('Continuar? [S/N] ')).upper()
    if resp in 'Nn':
        break
média = soma / len(lista)
print(lista)
print(f'O total de pessoas cadastradas foi {len(lista)}.')
print(f'A média de idade foi {média}.')
print('A lista com as mulheres é a seguinte...')
print(listafem)
print('A lista com as pessoas com idade superioar a média...')
print(maioridade)

