a=int(input('Primeiro Segmento'))
b=int(input('Segundo Segmento'))
c=int(input('Terceiro Segmento'))
if a==b==c:
    print('Seu triângulo é Equilatero.')
elif a != b and b != c and c != a:
    print('Seu triângulo é escaleno')
else:
    print('Seu triângulo é isosceles')