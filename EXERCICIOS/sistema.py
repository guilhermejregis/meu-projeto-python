from uteis.cores import *
def linha(tam=42):
    return( '-' * tam )


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU')
    print('1- Cadastrar Pessoas')
    print('2- Listar Pessoas')
    print('3- Sair')
    linha()
    resp = int(input('Sua opção: '))
    if resp.isnumeric():
        return resp
    else:
        print(f'{vermelho('ERRO! Digite um número inteiro válido.')}')
    if resp==1:
        cabecalho('OPÇÃO 1')
    if resp==2:
        cabecalho('OPÇÃO 2')
    if resp==3:
        cabecalho('Saindo do sistema...')

def cadastro(lista):
    cabecalho('CADASTRO')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))

pontos.sort()