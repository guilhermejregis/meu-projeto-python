vcasa= float(input('Qual o valor da casa?'))
anos=int(input('Em quantos anos pretende pagar?'))
pmensal= vcasa / (anos * 12)
print('A sua prestação mensal será de {}'.format(pmensal))
sal= float(input('Qual o seu salário?'))
if pmensal > (sal*30/100):
    print('O empréstimo foi negado, pois o valor de prestação mensal excede 30% do seu salário.')
else:
    print('O empréstimo foi aprovado.')