numeros= 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
n1=int(input('Digite um valor entre 0 e 10: '))
while True:
    if n1<=10:
        print(f'você digitou o número {numeros[n1]}')
    if n1>10:
        break



