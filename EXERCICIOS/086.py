smp=0
smt=0
maiorvalor=0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz [l] [c] = int(input(f'Digite um valor para [{l}], [{c}]: '))
        if matriz [l] [c] % 2 ==0:
            smp+= matriz [l] [c]
        smt+=matriz[l] [2]
        if matriz [1] [c] == 0:
            maiorvalor=matriz [1] [c]
        else:
            if matriz [1] [c] > maiorvalor:
                maiorvalor= matriz [1] [c]
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz [l] [c]:^5}]', end='')
    print()
print(f'A soma dos números pares digitados é igual a {smp}.')
print(f'A soma dos valores da terceira coluna é igual a {smt}')
print(f'O maior valor da segunda linha é {maiorvalor}.')

