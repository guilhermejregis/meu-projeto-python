from random import randint
n2=randint(1,10)
while True:
    if option == 0:
        break
    print('Vamos jogar par ou impar')
    print('''[1] Par [2] Impar''')
    option=int(input('Qual a sua opção? '))
    if option==1:
        print('Ok, sou ímpar.')
        n1=int(input('agora fale seu número: '))
        print(f'Meu número foi {n2} e o seu foi {n1}.')
        if (n2+n1)%2==0:
            print('Você Ganhou!')
        else:
            print('Você Perdeu!')
    else:
        print('Ok, sou ímpar.')
        n1=int(input('agora fale seu número: '))
        print(f'Meu número foi {n2} e o seu foi {n1}.')
        if (n2+n1)%2==0:
            print('Você Perdeu!')
        else:
            print('Você Ganhou!')
print('Fim do jogo')  