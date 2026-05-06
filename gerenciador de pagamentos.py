valor=int(input('Qual o valor do produto?'))
vista=str(input('O pagamento será em dinheiro ou cartão?').strip())
if (vista.upper()=='DINHEIRO'):
    print('O valor do seu produto fica {}'.format(valor - (valor*10/100)))
elif (vista.upper()=='CARTÃO'):
    forma=input('O pagamento será à vista, em 2x ou 3x?'.strip)
    if (forma.upper()=='À VISTA'):
        print('O valor do seu porduto fica {}'.format(valor- (valor*5/100)))
    elif (forma.upper()=='2X'):
        print('Seu valor total fica {}'.format(valor))
    else:
        print('Seu valor total fica {}'.format(valor+ (valor*20/100)))

