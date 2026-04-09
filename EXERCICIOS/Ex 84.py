dados=list()
princ=list()
totpessoas=0
mai=0
men=0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    totpessoas+=1
    princ.append(dados[:])
    if len(princ)==0:
        mai=men=dados[1]
    else:
        if dados[1]>mai:
            dados[1]=mai
        if dados[1] <men:
            dados[1] = men

    resp=str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print(princ)
print(f'O total de pessoas cadastradas foram {totpessoas}')
print(f'O maior peso foi de {mai}kg e o menor peso foi de {men}kg.')

