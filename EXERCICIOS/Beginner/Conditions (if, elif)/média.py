n1=float(input('Qual sua primeira nota?'))
n2=float(input('Qual sua segunda nota?'))
m=float((n1+n2)/2)
if m>=7:
    print('Parabéns você passou de ano, com média {}!'.format(m))
elif m>5 and m<6,9 :
    print('Voce está de recuperação, e sua média ficou {}.'.format(m))
elif m<5,0:
    print('Você está   brovado, com média {}.'.format(m))