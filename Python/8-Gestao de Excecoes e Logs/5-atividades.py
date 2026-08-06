# Atividades

'''1 - Crie uma função que receba duas strings que serão convertidas para 
números para serem somadas, se ao realizar o casting ocorrer um erro, gere 
uma exceção informando o motivo.'''
def soma(str1, str2):
    try:
        num1 = float(str1)
        num2 = float(str2)
        return num1 + num2
    except:
        raise Exception("Não foi possível fazer o casting das strings")

print(soma('1', '2'))

'''2 - Crie uma função que receba uma lista e um número e retorne o elemento 
da lista na posição deste número. Faça um tratamento para que caso haja um 
acesso fora do índice a função retorne o valor None.'''
def acessa_seguro(lista, indice):
    try:
        return lista[indice]
    except:
        return None

lista = [1]
print(acessa_seguro(lista, 1))

'''3 - Crie uma função que leia o input do usuário e retorne o que foi 
digitado, mas caso o input seja interrompido trate a exceção e retorne o 
valor None.'''
def le_input_seguro():
    try:
        return input("Digite algo: ")
    except:
        return None

print(le_input_seguro())

'''4 - Crie uma classe que represente um caractere (string de tamanho 1), use 
propriedades ou crie uma função para isso (mas deixe valor privado) e caso 
o usuário tente inserir um texto gere uma exceção dizendo o motivo.'''
class Caractere:
    def __init__(self, caractere):
        self.__caractere = ''
        self.caractere = caractere

    @property
    def caractere(self):
        return self.__caractere

    @caractere.setter
    def caractere(self, value):
        if len(value) > 1:
            raise Exception("Caractere deve ter no máximo tamanho 1")

        self.__caractere = value

letra = Caractere("a")
print(letra.caractere)

try:
    letra.caractere = 'ab'
except Exception as ex:
    print(ex)

print(letra.caractere)