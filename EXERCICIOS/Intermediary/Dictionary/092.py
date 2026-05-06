cadastro={}
cadastro['Nome']=str(input('Nome: ')).strip().upper()
cadastro['Ano']=int(input('Ano de nascimento: '))
cadastro['Idade']= 2026-cadastro['Ano']
cadastro['CTPS']=int(input('Carteira de trabalho: '))
if cadastro['CTPS']!=0:
    cadastro['Contratação']=int(input('Ano de contratação: '))
    cadastro['Salário']=float(input('Salário atual: '))
if cadastro['Idade']>=65:
    cadastro['Aposentadoria']='Liberado'
elif cadastro['Contratação']==2006:
    cadastro['Aposentadoria']='Liberado'
else:
    cadastro['Aposentadoria']='Não Liberado'
print(cadastro.items())