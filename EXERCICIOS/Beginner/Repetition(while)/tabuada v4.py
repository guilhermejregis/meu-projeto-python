import math
c=0
while True:
    n=int(input('Digite um número para ver sua tabuada: '))
    if n<0:
        break
    for c in range(1,10):
        c+=1
        print(f'{n}x{c}={n*c}')