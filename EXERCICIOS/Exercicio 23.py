import random
num = random.randint(0, 9999)
num = str(num)
print('Analisando seu número {}'.format(num))
print('unidade: {}'.format(num[3]))
print('dezena: {}'.format(num[2]))
print('centena: {}'.format(num[1]))
print('milhar: {}',format(num[0]))