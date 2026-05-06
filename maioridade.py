for c in range (1,8):
    ano=int(input('Digite um ano de nascimento:'))
maior=0
menor=0

if 2026-ano <= 18:
    maior += 1
else:
    menor += 1
print('Nesse grupo existem {} maiores de idade e {} menores de idade'.format(maior, menor))
