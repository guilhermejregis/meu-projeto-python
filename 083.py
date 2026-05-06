expressoes=[]
while True:
    r=str(input('Digite uma expressão utilizando parentêses (): ')).strip().capitalize()
    if '(' and ')' in r:
        expressoes.append(r)
    else:
        print('Inválido, utilize parentêses () corretamente.')
    if 'Parar' in r:
        break
print(f'As expressões citadas foram {expressoes}')