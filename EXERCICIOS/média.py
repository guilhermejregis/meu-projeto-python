boletim=[]
while True:
        nome=str(input('Digite seu nome: ')).strip().capitalize()
        nota1=float(input('Digite sua primeira nota: '))
        nota2=float(input('Digite sua segunda nota: '))
        média=(nota1+nota2)/2
        boletim.append([nome, [nota1, nota2], média])
        resp=str(input('Quer continuar? [S/N] '))
        if resp in 'Nn':
            break
print(boletim, end='')
print()


