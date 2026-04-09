numeros=0
valores= [[], []]
for c in range (0,7):
    numeros.append(int(input('Digite um número: ')))
    if numeros[0]%2==0:
        valores[0].append(numeros)
    else:
        valores[1].append(numeros)
print(valores.sort())


