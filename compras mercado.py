preço=totcompra=mil=0
nomemenos=''
customenos=0
while True:
    nome= ' '
    nome=str(input('Nome do Produto: ')).strip().capitalize()
    preço=float(input('Preço do produto: '))
    totcompra+=preço
    if preço>=1000:
        mil+=1
    if preço<preço:
        preço=customenos
        nome=nomemenos
    opt= ' '
    while opt not in 'SN':
        opt=str(input('Quer continuar? [S/N]: ')).strip().upper()
    if opt == 'N':
        break
print(f'Total da compra: R$ {totcompra:,.2f} ')
print(f'Total de {mil} produtos custam mais que R$ 1000.')
print(f'O produto mais barato é o/a {nomemenos} e custa R${customenos} ')
