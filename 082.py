valores=[]
par=[]
impar=[]
while True:
    n=int(input('Digite um valor: '))
    valores.append(n)
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
    if n==0:
        break
par.pop()
print(f'A Lista total ficou igual a, {valores}')
print(f'A lista apenas com números pares ficou igual a {par}')
print(f'A lista apenas com números impares ficou igual a {impar}')