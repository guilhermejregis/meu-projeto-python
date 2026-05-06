valores=list()
while True:
    n=int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
    else:
        print('Valor repetido, digite outro valor!')
    resp=str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp=='N':
        break
print('Sua lista ficou assim...')
valores.sort()
print(valores)