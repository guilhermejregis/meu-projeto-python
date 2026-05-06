s = 0
for c in range (1,7):
    num=int(input('Digite um valor inteiro:'))
    if num%2==0:
        s+=num
print('A soma dos números pares é igual a {}'.format(s))