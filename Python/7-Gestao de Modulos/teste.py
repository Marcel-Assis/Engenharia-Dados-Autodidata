'''
Este é o arquivo principal contendo uma variável chamada PI, uma função chamada soma e uma classe chamada Teste
'''

PI = 3.1415

class Teste:
    '''Classe de teste'''
    def __init__(self):
        print('Classe teste')

def MyFunc(num):
    '''Função de teste que imprime o número recebido como parâmetro'''
    print(num)

def soma(num1, num2):
    '''Função que retorna a soma de dois números recebidos como parâmetros'''
    return num1 + num2

print(__doc__) # Exibe a documentação do módulo
print(soma.__doc__) # Exibe a documentação da função soma

#help(soma) # Exibe a ajuda interativa da função soma