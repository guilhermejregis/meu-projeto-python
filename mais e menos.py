n1=int(input('Digite um valor: '))
cont=(0)
s1=(0)
while n1 != 999:
    cont+=1
    s1+=n1
    n1 = int(input('Quer continuar? Se sim digite oyutro número, se não digite 999: '))
m= s1 / cont
print(f'O total de algarismos digitados foram {cont} e a média deles foi {m}.')