v1=int(input('Qual a sua velocidade?'))
if v1>=80:
    a= v1-80
    m= a*7
    print('Você foi multado em R${}, por exceder a velocidade em {} km/h.'. format(m,a))
else:
    print('Você está dentro do limite de velocidade.')