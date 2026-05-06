tabela='corinthians', 'palmeiras', 'flamengo', 'santos', 'fluminense', 'botafogo', 'cruzeiro', 'Atlético Mineiro', 'chapecoense', 'Atlético Paranaense'
print('os 5 primeiros colocados são, ', end='')
print(tabela[:5])
print('Os ultimos 4 colocados são ', end ='')
print(tabela[6:])
print(sorted(tabela))
print(tabela.index('chapecoense'))