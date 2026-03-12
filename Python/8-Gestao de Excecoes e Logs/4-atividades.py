'''1 - Crie uma função que receba duas strings que serão convertidas para
números para serem somadas, se ao realizar o casting ocorrer um erro, gere
uma exceção informando o motivo'''
def soma(str1, str2):
    try:
        num1 = float(str1)
        num2 = float(str2)
        return num1 + num2
    except:
        raise Exception("Falha no casting")
print(soma('1', '2'))

'''2 - Crie uma função que receba uma lista e um número e retorne o elemento
da lista na posição deste número. Faça um tratamento para que caso haja um
acesso fora do índice a função retorne o valor None.'''
def acessa_seguro(lista, num):
    try:
        return lista[num]
    except IndexError as indexErr:
        return None
lista = ['a', 'b']
print(acessa_seguro(lista, 2))

'''3 - Crie uma função que leia o input do usuário e retorne o que foi
digitado, mas caso o input seja interrompido trate a exceção e retorne o
valor None.'''
def input_seguro():
    try:
        return input("Digite algo: ")
    except:
        return None
print(input_seguro())

'''4 - Crie uma classe que represente um caractere (string de tamanho 1), use
propriedades ou crie uma função para isso (mas deixe valor privado) e caso
o usuário tente inserir um texto gere uma exceção dizendo o motivo.'''
class Caracter:
    def __init__(self, caracter):
        self.__caracter = ''
        self.caracter = caracter
    @property
    def caracter(self):
        return self.__caracter
    @caracter.setter
    def caracter(self, value):
        if len(value) > 1:
            raise Exception("Caractere deve ter no máximo tamanho 1")
        self.__caracter = value
letra = Caracter("a")
print(letra.caracter)

try:
    letra.caracter = 'ab'
except Exception as ex:
    print(ex)