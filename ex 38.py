n1=int(input('Me fale um número inteiro'))
n2=int(input('Me fale outro número inteiro'))
if n1>n2:
    print('O {} é maior que {}'.format(n1, n2))
elif n2>n1:
    print('O {} é maior que {}'.format(n2, n1))
elif n1==n2:
    print('Os valores {} e {} são iguais'.format(n1, n2))

