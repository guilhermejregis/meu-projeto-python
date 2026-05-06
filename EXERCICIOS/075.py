n=(int(input('Digite um valor:')),
   int(input('Digite outro valor: ')),
   int(input('Digite mais um valor: ')),
   int(input('Digite o ultimo valor: ')))
print('Os números citados foram: ')
print(n)
print('-='*30)
print('O número 9 apareceu: ')
print(n.count(9))
print('-='*30)
print('Em qual posição apareceu o número 3 primeiro: ')
if 3 in n:
    print(n.index(3))
else:
    print('Número 3 não apareceu.')
print('-='*30)
for c in n:
    if c%2==0:
        print(c, end=' ,')