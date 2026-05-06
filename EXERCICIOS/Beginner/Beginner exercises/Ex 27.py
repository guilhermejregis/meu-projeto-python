nome = str(input('Digite seu nome completo')).strip()
print('Seu primeiro nome é {}'.format(nome.split()[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))