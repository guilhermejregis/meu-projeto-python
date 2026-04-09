car={}
valores=[]
while True:
    car['Nome']=str(input('Nome: ')).upper()
    car['Partidas']=int(input('Quantas partidas jogou? '))
    for c in range(car['Partidas']):
        car['Gols']=int(input((f'Quantos gols na partida {c+1}: ')))
        if car['Gols']==0:
            car['Gols']=0
    resp=str(input('Quer continuar? '))
    if resp in 'Nn':
        break
print('-='*30)
print('Nome      ', end='')
print('Gols      ', end='')
print('Total')
print('-'*30)
valores.append(car.values())
print(valores)

