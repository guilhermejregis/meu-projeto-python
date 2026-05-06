nome=str(input('Digite seu nome:')).upper().strip()
print('Seu nome tem {} letras A'.format(nome.count('A')))
print("A primeira letra A apareceu na posição {}".format(nome.find('A')+1))
print('A última letra A apareceu na posição {}'.format(nome.rfind('A')+1))
