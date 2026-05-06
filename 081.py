valores=list()
while True:
    n=int(input('Digite um valor: '))
    valores.append(n)
    resp=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp=='N':
            break
valores.sort(reverse=True)
print(f'foram digitados exatamente {len(valores)} números.')
print (valores)
if 5 in valores:
    print(f'O número 5 foi citado {valores.count(5)} vezes')
else:
    print('O númetro 5 não foi citado')