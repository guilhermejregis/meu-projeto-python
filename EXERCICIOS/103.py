def ficha(n1, g1):
    print(f'O jogador {n1} marcou {g1} gols no campeonato.')


nome=str(input('Nome do Jogador: '))
gols=str(input('Gols: '))
ficha(nome, gols)
if g1.isnumeric():
    int(g1)
else:
    g1 = 0
if n1.strip() == '':
    ficha(gols=g1)
else:
    ficha(n1, g1)

