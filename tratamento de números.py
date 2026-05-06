cont=0
n1=0
s1=0
while n1 != 999:
    n1=int(input('Digite um número: '))
    cont+=1
    s1+=n1
print('Você digitou {} e a soma de todos os algarismos digitados é igual a {}'.format(cont-1, s1-999))
print('Fim')
