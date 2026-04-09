boletim={}
boletim['nome']=str(input('Digite seu nome: ')).capitalize()
boletim['média']=float(input('Digite sua média: '))
if boletim['média']<6.0:
    boletim['situação']='Recuperação'
else:
    boletim['situação']='Aprovado'
print(boletim)