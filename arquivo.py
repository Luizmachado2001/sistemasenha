"""
1: Esse sistema vai criar uma senha
2: ele armazena essa senha
3: depois vocÊ tentar loogar com sua senha
"""


def criar_senha():
    global senha    
    senha = input('Digite uma senha: ')
    return senha

def comparar_senha():
    global nova
    nova = input('Digite a senha:')
    if nova == senha:
        print('você logou')
    else:
        print('\nVocê errou sua senha!\n')
        comparar_senha()


def logar():
    criar_senha()
    comparar_senha()


logar()