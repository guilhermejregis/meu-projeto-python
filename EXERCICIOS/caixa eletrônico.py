n1=int(input('Valor: R$'))
total=n1
céd=50
totcéd=0
while True:
    if total>=50:
        total-=50
        totcéd+=1
    else:
        if totcéd>0:
            print(f'O total de {totcéd} cédulas de R${céd} foram sacados.')
        if céd==50:
            céd==20
        elif céd==20:
            céd==10
        elif céd==10:
            céd==1
        if total==0:
            break
print(f'O total de {totcéd} cédulas de R${céd} foram sacados.')

