n=0
s1=0
cont=0
while True:
    n=int(input('Digite um valor: '))
    if n == 999:
        break
    cont+=1
    s1+=n
print(f'A soma entre os {cont} algarismos digitados é igual a {s1}')