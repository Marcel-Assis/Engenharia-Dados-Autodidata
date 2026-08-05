# Criando e Lendo Ajuda de Módulos

import sys
print(sys.__doc__) # documentação do módulo sys

# para criar a documentação do módulo, utilizar três aspas simples no início do módulo
# exemplo:

'''
Este é o arquivo principal contendo uma variável chamada euler e uma função chamada soma
'''
euler = 2.71828
def soma(num1,num2):
    ''' Função que soma dois números recebidos por  entrada '''
    return num1 + num2

print(soma.__doc__) # trás a documentação da função
print(help(soma)) # trás informações da função