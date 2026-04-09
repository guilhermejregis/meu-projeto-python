from random import randint
maiorvalor=0
maiorjogador=''
dado={'Jogador 1': randint(1,6),
      'Jogador 2': randint(1,6),
      'Jogador 3': randint(1,6),
      'Jogador 4': randint(1,6)}
print('valores sorteados')
for k, v in dado.items():
    print(f'O {k} tirou {v}')
    if k is None:
        maiorvalor=None
    else:
        if v>maiorvalor:
            maiorvalor=v
            maiorjogador=k
print('O vencedor foi')
print(f'O maior valor foi {maiorvalor} do {maiorjogador}.')

