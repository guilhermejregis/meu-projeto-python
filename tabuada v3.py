n1 = int(input('Primeiro Valor:'))
n2= int(input('Segundo termo:'))
maiornumero = 0
ação = 0
while ação != '5':
    print('-------------------'
      '[1] Somar'
      '[2] Multiplicar'
      '[3] Maior'
      '[4] Novos Números'
      '[5] Sair'
      '--------------------')
    ação= str(input('Qual sua escolha?'))
    if ação == '1':
        print('A soma entre {} e {} é {}'.format(n1, n2, n1+n2))
    elif ação == '2':
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
    elif ação == '3':
        if n1 > n2:
            maiornumero = n1
        else:
            maiornumero = n2
        print('O maior número entre {} e {} é {}'.format(n1, n2, maiornumero))
    elif ação == '4':
        print('Escolha novos números')
        n1=int(input('Primeiro termo:'))
        n2=int(input('Segundo termo:'))
print('Fim do Jogo')


