def leiaint(msg):


    if msg.isnumeric():
        int(msg)
        print(f'Você digitou o número {msg}')
    else:
        return f'O caracter {msg} não é um número.'

n = leiaint('Digite um numero inteiro qualquer: ')