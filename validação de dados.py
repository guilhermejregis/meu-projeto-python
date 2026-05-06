sexo=str(input('Qual seu sexo? [M/F]')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados Inválidos, por favor informe corretamente.')).strip().upper()
if sexo == 'M':
    print('Sexo Masculino cadastrado.')
elif sexo == 'F':
    print('Sexo Feminino Cadastrado')






