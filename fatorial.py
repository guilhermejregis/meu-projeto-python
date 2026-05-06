import math
n1=int(input('Digite um Valor:'))
f=math.factorial(n1)
c = n1
while c > 0:
    print(' {} '.format(c),end='')
    print('x' if c > 1 else '=', end='')
    print(' {}'.format(f),end='')
    c -= 1
