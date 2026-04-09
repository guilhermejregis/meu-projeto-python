from random import randint


def sorteia(num):
    for c in range(0,5):
       n=randint(0,10)
       numeros.append(n)
       print(f'{n} ', end='')



def somapar(par):
    somatorio=0
    for valor in numeros:
        if valor%2==0:
            somatorio+=valor
    print(somatorio)

numeros=list()
print('Os números sorteados foram...')
sorteia(numeros)
print()
print('-='*30)
print('A soma dos números pares sorteados ficou igual a ...')
somapar(numeros)
