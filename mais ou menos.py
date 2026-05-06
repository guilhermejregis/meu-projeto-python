import random
palpite = 0
n1= random.randint(1,10)
print('Sou seu computador')
print('Acabei de pensar em um númeor de 1 a 10...')
print('Tente adivinhar e indicarei se é menor ou maior que seu palpite')
acertou = False
while not acertou:
    n2 = int(input('Qual seu Palpite?'))
    palpite += 1
    if n1 == n2:
           acertou = True
    elif n1 > n2:
            print('Mais, tente novamente:')
    elif n1 < n2:
            print('Menos, tente novamente:')
print('Acertou com um total de {} palpites.'.format(palpite))
