from random import randint

print('JOGOS DA MEGASENA')
print('-='*30)
c=int(input('Números de jogos: '))
for i in range(c):
        print(f'Jogo {i+1}: ', end='')
        print([randint(1,60)], [(randint(1,60))], [(randint(1,60))], [(randint(1,60))], [(randint(1,60))], [(randint(1,60))])