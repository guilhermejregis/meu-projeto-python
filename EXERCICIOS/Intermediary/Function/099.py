def maior(*num):
    maiorvalor = cont = 0
    for valor in num:
        cont+=1
        if cont==1:
            valor=maiorvalor
        else:
            if valor>maiorvalor:
                maiorvalor=valor
    print(f'O maior valor desses citados é {maiorvalor}')
maior(10, 22, 6, 4, 2, 160)