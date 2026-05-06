carreira={}
carreira['Nome:']=str(input('Nome: ')).upper()
carreira['Partidas:']=int(input('Total de Partidas: '))
carreira['Gols:']=int(input('Total de Gols: '))
carreira['G/P:']= carreira['Gols:'] / carreira['Partidas:']
print(carreira)